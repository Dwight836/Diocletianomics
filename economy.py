import random as rnd
import numpy as np
import copy

from citizen import Citizen
from aristocrat import Aristocrat
from firm import Firm


class Economy:
    history = []

    def __init__(self):

        self.goods = dict()
        self.connectivity = 1
        self.citizens = []
        self.firms = []
        self.workforce = []
        self.aristocrats = []

        # self.barriers_to_entry = {}
        self.barriers_to_entry = 0

        self.fixed_costs = None

        self.markets = []
        # Retirement age should be an eco wide variable...maybe
        # self.retirement_age = 60

    def add_citizen(self, citizen):
        # Adds one citizen to the economy, adjusting demand
        self.citizens.append(citizen)
        self.add_demand()

    def introduce_citizens(self, n=1000):
        # Batch introduces n citizens
        for _ in range(n):
            c = Citizen()
            self.add_citizen(c)

            # Batching 1% of aristocrats
            if _ % 100 == 0:
                a = Aristocrat(eco=self)
                self.add_citizen(a)

    def introduce_goods(self, goods_list):
        # Introduces goods, initializing supply at 0
        for good in goods_list:
            self.introduce_good(good)

    def introduce_good(self, good):
        # this has the option of adding a good (silk?) to the economy)
        # pseudocode framework...
        # // for mkt in self.markets:
        # self.goods[mkt][good] = dc

        self.goods[good] = {'quantity_demanded': 0,
                            'quantity_supplied': 0,
                            'demand_weight': np.random.default_rng().normal(1, 0.10, 1)[0] * self.connectivity,
                            'cost_weight': (np.random.default_rng().normal(1, 0.10, 1)[0]) / self.connectivity,
                            'price': 1}

    def add_demand(self):
        # This adds a consumer to already existing demand structure
        pop = len(self.citizens)
        for good in self.goods.keys():
            self.goods[good]['quantity_demanded'] *= ((pop+1)/pop)

    def adjust_demand(self):
        # Adjusts demand based on population from base values
        population = len(self.citizens)
        for good in self.goods.keys():

            # /// maybe make existing weight shift rather than generating new float...
            weight = np.random.default_rng().normal(loc=self.goods[good]['demand_weight'], scale=0.01, size=1)[0]
            self.goods[good]['demand_weight'] = weight
            self.goods[good]['quantity_demanded'] = weight * population

    def get_workforce(self):
        # Updates the workforce of the economy
        self.workforce = [citizen for citizen in self.citizens if (citizen.workforce and citizen.alive)]

    def get_citizens(self):
        # Updates the population of the economy
        self.citizens = [citizen for citizen in self.citizens if citizen.alive]

    def get_aristocrats(self):
        # Updates aristocrat population
        self.aristocrats = [Aristocrat(citizen) for citizen in self.citizens if citizen.job == 'nobility']
        for aristocrat in self.aristocrats:
            aristocrat.eco = self

    def employ_workers(self):
        # I would eventually like weights to be wages or some measure
        weights = None
        firm_ids = [firm.firm_id for firm in self.firms]
        choices = rnd.choices(firm_ids, weights=weights, k=len(self.workforce))

        for worker, choice in zip(self.workforce, choices):
            if worker.job is None:
                self.firms[choice].hire_worker(worker)

    def introduce_workers(self):
        self.get_workforce()
        self.employ_workers()

    def introduce_firms(self):
        for good in self.goods.keys():
            self.introduce_firm(good)

    def introduce_firm(self, good, owner=None):
        f = Firm(good=good, eco=self, owner=owner)
        self.firms.append(f)

    def production_cycle(self):
        # Runs production cycle for non-bankrupt firms
        self.firms = [firm for firm in self.firms if firm.open]
        for firm in self.firms:
            firm.pass_year()

    def set_prices(self):
        # Placeholder method before market integration
        for good in [firm.good for firm in self.firms]:

            weighed_outputs = []
            outputs = []

            # for each firm producing that good
            for firm in self.firms:
                if firm.good == good and firm.inventory[good] > 0:
                    weighed_outputs.append(firm.find_average_cost() * firm.inventory[good])
                    outputs.append(firm.inventory[good])

            # If lists exist
            if weighed_outputs and outputs:

                weighed_prod = sum(weighed_outputs)
                total_prod = sum(outputs)

                if 0 not in (weighed_prod, total_prod):
                    weighted_avg_price = weighed_prod / total_prod

                else:
                    weighted_avg_price = 1
                self.goods[good]['price'] = weighted_avg_price

    def consume_goods(self):
        # Resets supplies
        for good in self.goods.keys():
            self.goods[good]['quantity_supplied'] = 0

    def get_barriers(self):
        # Business owners as proportion of aristocracy
        business_owners = [aristocrat for aristocrat in self.aristocrats if aristocrat.entrepreneur]

        # This populates the barriers to entry dictionary, starting at 0
        if len(self.citizens) != 0 and len(self.aristocrats) != 0:

            for good in self.goods.keys():
                self.barriers_to_entry[good] = 0




    def pass_year(self):
        # Population consumes goods, zeroing supply
        self.consume_goods()

        # Passes a year for every citizen
        for citizen in self.citizens:
            citizen.pass_year()

            baby = citizen.reproduce()
            if baby:
                self.add_citizen(baby)

        # Passes fiscal years for aristocrats
        for aristocrat in self.aristocrats:
            aristocrat.pass_fiscal_year()

        # Adjusts citizens and aristocrats
        self.get_citizens()
        self.get_aristocrats()

        # Adjusts demand and workforce based on population
        self.adjust_demand()
        self.get_workforce()
        self.employ_workers()

        # Produces goods and sends report
        self.production_cycle()
        self.set_prices()

        Economy.history.append(copy.deepcopy(self))

    def simulate(self, n_years=25, n_citizens=100,
                 goods=('pottery', 'bricks', 'glass', 'metal', 'ships', 'wrought iron', 'processed fish', 'silk')):
        # Runs basic simulation with default kwargs
        self.introduce_goods(goods)
        self.introduce_citizens(n=n_citizens)
        self.introduce_firms()
        self.introduce_workers()

        ct = 0
        while ct < n_years:
            self.pass_year()
            ct += 1
