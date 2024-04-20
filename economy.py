import random as rnd
import numpy as np

from citizen import Citizen
from firm import Firm


class Economy:

    def __init__(self):

        self.goods = dict()
        self.connectivity = 1
        self.citizens = []
        self.firms = []
        self.workforce = []

    def add_citizen(self, citizen):
        # Adds a specific citizen to the economy, adjusting demand accordingly
        self.citizens.append(citizen)
        self.add_demand()

    def introduce_citizens(self, n=1000):
        # Batch introduces n citizens to the economy
        for _ in range(n):
            self.add_citizen(Citizen())

    def introduce_goods(self, goods_list):
        # Introduces goods to the economy, initializing supply at 0
        for good in goods_list:
            self.introduce_good(good)

    def introduce_good(self, good):
        # this has the option of adding a good (silk?) to the economy)
        self.goods[good] = {'quantity_demanded': 0,
                            'quantity_supplied': 0,
                            'demand_weight': np.random.default_rng().normal(1, 0.10, 1)[0] * self.connectivity,
                            'cost_weight': (np.random.default_rng().normal(1, 0.10, 1)[0]) / self.connectivity}

    def add_demand(self):
        # This adds a consumer to already existing demand structure
        pop = len(self.citizens)
        for good in self.goods.keys():
            self.goods[good]['quantity_demanded'] *= ((pop+1)/pop)

    def adjust_demand(self):
        # Adjusts demand based on population from base values
        population = len(self.citizens)
        for good in self.goods.keys():
            weight = np.random.default_rng().normal(1, 0.05, 1)[0]
            #print(f'dem_weight {good} = {dem_weight}')

            self.goods[good]['demand_weight'] = weight
            #self.goods[good]['quantity_demanded'] = self.goods[good]['demand_weight'] * population
            self.goods[good]['quantity_demanded'] = weight * population

    def get_workforce(self):
        # Updates the workforce of the economy
        self.workforce = [citizen for citizen in self.citizens if (citizen.workforce and citizen.alive)]

    def get_citizens(self):
        # Updates the population of the economy
        self.citizens = [citizen for citizen in self.citizens if citizen.alive]

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

    def introduce_firm(self, good):
        f = Firm(good=good, eco=self)
        self.firms.append(f)

    def production_cycle(self):
        # Runs the production cycle for each firm
        for firm in self.firms:
            firm.produce()

    def consume_goods(self):
        # Resets supplies
        for good in self.goods.keys():
            self.goods[good]['quantity_supplied'] = 0

    def pass_year(self, report=False):
        # Population consumes goods, zeroing supply
        self.consume_goods()

        # Passes a year for every citizen
        for citizen in self.citizens:
            citizen.pass_year()

            if citizen.reproduce():
                baby = Citizen(set_age=0)
                self.citizens.append(baby)

        # Adjusts citizen list
        self.get_citizens()

        # Adjusts demand and workforce based on population
        self.adjust_demand()
        self.get_workforce()
        self.employ_workers()

        # Produces goods and sends report
        self.production_cycle()

        if report:
            self.report(age=True, workforce=True, good='silk')

    def report(self, good=None, age=None, workforce=None):

        if good:
            print(f'{self.goods_supplied[good]:.2f} units of {good}')

        if age:
            ages = [citizen.age for citizen in self.citizens]
            avg = sum(ages)/len(ages)
            print(f'{len(self.citizens)} citizens w/Average Citizen age {avg:.2f}')

        if workforce:
            workforce_ages = [worker.age for worker in self.workforce]
            avg = sum(workforce_ages)/len(workforce_ages)
            print(f'{len(self.workforce)} workers w/ Average Worker age {avg:.2f}')













