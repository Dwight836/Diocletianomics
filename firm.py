import numpy as np


class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None):
        # Each firm produces a good
        self.good = good
        self.eco = eco
        self.workers = []
        self.productivity = np.random.default_rng().normal(1, 0.1, 1)[0]
        self.inventory = {self.good: 0}

        # Not going to add Account class yet, don't want another point of failure
        self.balance = 0
        self.income = 0
        self.markup = 0.2

        self.market = None

        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def __repr__(self):
        return f'{self.productivity:.3f}x -- {self.good}_#{self.firm_id} firm, employing {len(self.workers)} workers'

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
            self.inventory[self.good] = output

    def hire_worker(self, worker):
        # Worker is a citizen object
        self.workers.append(worker)
        worker.job = self.good

    def audit_workforce(self):
        # This clears the firm of retired / dead employees
        self.workers = [worker for worker in self.workers if worker.workforce]

    def set_wages(self):
        # Sets a wage for each worker
        for worker in self.workers:
            wage = worker.productivity
            worker.wage = wage

    def pay_wages(self):
        # Pays wages
        for worker in self.workers:
            worker.balance += worker.wage

    def pass_year(self):
        self.set_wages()
        self.pay_wages()

    def find_cost(self):
        # Avg cost per 1 good produced
        avg_labor = sum([worker.wage for worker in self.workers]) / self.inventory[self.good]
        materials = self.eco.goods[self.good]['cost_weight']
        cost = (avg_labor + materials) * (1 + self.markup)
        return cost

    def compete(self):
        # if market price is lower than internal cost, reduces profit margin
        # // Not in play yet. Very simple competition.
        competitors = [firm for firm in self.eco.firms if
                       (self.good == firm.good and
                        self.firm_id != firm.firm_id)]
        
        if len(competitors) > 0:
            if self.eco.goods[self.good]['price'] < self.find_cost():
                self.markup -= 0.01
                # print(f'firm {self.firm_id} reduces profit margins')


