import numpy as np
import random as rnd


class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None, owner=None):
        # Each firm produces a good
        self.good = good
        self.eco = eco
        self.workers = []
        # self.productivity = np.random.default_rng().normal(1, 0.1, 1)[0]
        self.productivity = rnd.uniform(0.8, 1.2)
        self.inventory = {self.good: 1}

        self.balance = 1000
        self.income = 0
        self.markup = 0.2

        self.market = None

        # KWARG
        self.owner = owner

        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def __repr__(self):
        return f'{self.productivity:.3f}x -- {self.good}_#{self.firm_id} firm, employing {len(self.workers)} workers'

    def pass_year(self):
        # I want to everything into this one method
        self.audit_workforce()
        self.set_wages()
        self.produce()

        self.sell_goods()
        self.pay_costs()
        self.pay_wages()

        self.compete()

    def produce(self):
        # comment...
        worker_prod = sum([worker.productivity for worker in self.workers])
        output = worker_prod * self.productivity

        # if a firm is IN an economy, sends goods to that market
        if self.eco:
            if self.good in self.eco.goods.keys():
                self.eco.goods[self.good]['quantity_supplied'] += output

        if self.good:
            self.inventory[self.good] = output

    def hire_worker(self, worker):
        # Worker is a citizen object
        self.workers.append(worker)
        worker.job = self.good

    def audit_workforce(self):
        # This clears the firm of retired / dead employees
        self.workers = [worker for worker in self.workers if worker.workforce and worker.alive]

    def set_wages(self):
        # Sets a wage for each worker
        for worker in self.workers:
            # Add additional rnd?
            wage = (1 + worker.productivity**2)
            worker.wage = wage

    def pay_wages(self):
        # Pays wages
        for worker in self.workers:
            worker.balance += worker.wage
            self.balance -= worker.wage

    def find_average_cost(self):
        if self.workers:
            # Avg cost per 1 good produced IF firm has employees
            avg_labor = sum([worker.wage for worker in self.workers]) / self.inventory[self.good]
            materials = self.eco.goods[self.good]['cost_weight']
            cost = (avg_labor + materials) * (1 + self.markup)
            return cost
        else:
            return 1

    def sell_goods(self):
        # Sells inventory at market price
        if self.eco:
            revenue = self.inventory[self.good] * self.eco.goods[self.good]['price']
            self.income = revenue
            self.balance += revenue

    def pay_costs(self):
        # Pays for materials

        if self.eco:
            obligations = self.inventory[self.good] * self.eco.goods[self.good]['cost_weight']
            self.balance -= obligations

    def compete(self):
        # if market price is lower than internal cost, reduces profit margin
        if self.eco:

            competitors = [firm for firm in self.eco.firms if
                           (self.good == firm.good and
                            self.firm_id != firm.firm_id)]

            # if len(competitors) > 0:
            if competitors:
                # if marking up and non-competitive
                if self.eco.goods[self.good]['price'] < self.find_average_cost()\
                        and self.markup > 0:
                    self.markup -= 0.01
                    # print(f'firm {self.firm_id} reduces profit margins')
                else:
                    # self.markup += 0.01
                    pass




