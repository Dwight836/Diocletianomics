import random as rnd
import numpy as np

from citizen import Citizen
from firm import Firm


class Economy:

    def __init__(self):

        self.demand_weights = dict()
        self.goods_demanded = dict()
        self.goods_supplied = dict()
        self.citizens = []
        self.firms = []
        self.workforce = []

    def add_citizen(self, citizen):
        # Adds a specific citizen to the economy, adjusting demand accordingly
        self.citizens.append(citizen)
        # Hmmmmmm, this might be problematic later...
        # self.adjust_demand()

    def introduce_citizens(self, n=1000):
        # Batch introduces n citizens to the economy
        for _ in range(n):
            self.add_citizen(Citizen())

    def introduce_goods(self, goods_list):
        # Introduces goods to the economy, initializing supply at 0
        for good in goods_list:
            self.demand_weights[good] = np.random.default_rng().normal(1, 0.10, 1)[0]
            self.goods_demanded[good] = 0
            self.goods_supplied[good] = 0

    def adjust_demand(self):
        # Adjusts demand based on population from base values
        population = len(self.citizens)
        for good, quantity_demanded in self.goods_demanded.items():
            # print(len(self.goods_demanded))
            self.goods_demanded[good] = self.demand_weights[good] * population
            # self.goods_demanded[good] = quantity_demanded
            self.demand_weights[good] = np.random.default_rng().normal(1, 0.05, 1)[0]

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
            self.firms[choice].hire_worker(worker)

    def introduce_workers(self):
        self.get_workforce()
        self.employ_workers()

    def introduce_firms(self):
        for good in self.goods_demanded.keys():
            f = Firm(good=good, eco=self)
            self.firms.append(f)

    def production_cycle(self):
        # Runs the production cycle for each firm
        for firm in self.firms:
            firm.produce()

    def consume_goods(self):
        # Resets supplies
        for good in self.goods_supplied.keys():
            self.goods_supplied[good] = 0

    def pass_year(self):

        for citizen in self.citizens:
            citizen.pass_year()

            if citizen.reproduce():
                self.citizens.append(Citizen(set_age=0))

        # Adjusts citizen list
        self.get_citizens()

        # Adjusts demand and workforce based on population
        self.adjust_demand()
        self.get_workforce()

        # Produces goods and sends report
        self.production_cycle()
        # self.report(age=True, workforce=True)

        # Population consumes goods, zeroing supply
        self.consume_goods()

    def report(self, good=None, age=None, workforce=None):

        if good:
            print(f'{self.goods_supplied[good]:.2f} units of {g}')

        if age:
            ages = [citizen.age for citizen in self.citizens]
            avg = sum(ages)/len(ages)
            print(f'Average Citizen age {avg:.2f}')

        if workforce:
            workforce_ages = [worker.age for worker in self.workforce]
            avg = sum(workforce_ages)/len(workforce_ages)
            print(f'Average Worker age {avg:.2f}')









