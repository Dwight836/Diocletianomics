import numpy as np


class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None):
        # Each firm produces a good
        self.good = good
        self.eco = eco
        self.workers = []
        # imperial factories should be set at 1?
        #self.productivity = np.random.default_rng().normal(1, 0.1, 1)[0]
        self.productivity = 1
        self.inventory = {self.good: 0}
        # Not going to add Account class yet, don't want another point of failure
        self.balance = 0
        self.income = 0

        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def __repr__(self):
        return f'{self.good}_#{self.firm_id} firm, employing {len(self.workers)} workers'

    def produce(self):
        # comment...
        worker_prod = sum([worker.productivity for worker in self.workers])
        output = worker_prod * self.productivity
        # if a firm is IN an economy, sends goods to that market
        # // not going to alter structure rn
        if self.eco:
            if self.good in self.eco.goods.keys():
                self.eco.goods[self.good]['quantity_supplied'] += output
                # print('output updates')

        if self.good:
            # self.inventory[self.good] += output
            self.inventory[self.good] = output
            # pass

    def hire_worker(self, worker):
        # Worker is a citizen object
        self.workers.append(worker)
        worker.job = self.good

    def set_wage(self):
        # Sets a wage for each worker
        for worker in self.workers:
            wage = worker.productivity
            worker.wage = wage

    def pay_wage(self):
        # Pays wages
        for worker in self.workers:
            worker.balance += worker.wage

    def find_cost(self):
        # Cost of labor, materials, profit
        pass

    def set_price(self):
        # Adds market price...
        pass


