import numpy as np
import random as rnd


class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None, owner=None, starting_balance=1000):

        self.good = good
        self.eco = eco
        self.workers = []
        self.productivity = rnd.uniform(0.8, 1.2)
        self.inventory = {self.good: 1}
        self.open = True

        self.years_open = 0

        # Firm structure could be 1-2D Array as well
        self.balance = starting_balance * (1 - self.eco.barriers_to_entry) # // Just a float. Could be KV Pair...
        self.income = 0
        self.markup = 0.2

        self.market = None
        self.owner = owner

        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def __repr__(self):
        return f'{self.productivity:.3f}x -- {self.good}_#{self.firm_id} firm, employing {len(self.workers)} workers'

    def pass_year(self):
        # I want to put everything into this one method
        self.audit_workforce()
        self.set_wages()
        self.produce()

        self.sell_goods()
        self.pay_costs()
        self.pay_wages()

        self.compete()
        if self.open:
            self.years_open += 1

    def produce(self):
        # comment...
        # This is the production function
        worker_prod = sum([worker.productivity for worker in self.workers])
        output = worker_prod * self.productivity

        # if a firm is IN an economy, sends goods to that market
        if self.eco:
            if self.good in self.eco.goods.keys():
                self.eco.goods[self.good]['quantity_supplied'] += output

        # If firm in business,
        if self.good:
            self.inventory[self.good] = output

    def hire_worker(self, candidate):
        simple_selection = False
        complex_selection = not simple_selection

        if simple_selection:

            self.workers.append(candidate)
            candidate.job = self.good

        if complex_selection:
            # Worker is a citizen object, modified by relationship with the firm
            desired_salary = self.get_wage(candidate, report=True)
            predicted_contrib = self.get_marginal_product(candidate)

            # If non-blacklisted worker can make a positive impact
            if (desired_salary <= predicted_contrib) and (self.firm_id not in candidate.rejected_companies):
                self.workers.append(candidate)
                candidate.job = self.good
            else:
                # candidate is rejected and blacklisted
                candidate.rejected_companies.add(self.firm_id)

    def audit_workforce(self):
        # This clears the firm of retired / dead employees
        self.workers = [worker for worker in self.workers
                        if worker.workforce and worker.alive]

    def get_wage(self, worker, report=False):
        # This change is untested. Surely it will be fine.
        worker.wage = (1 + worker.productivity ** 2)
        if report:
            return worker.wage


    def set_wages(self):
        # Sets a wage for each worker
        for worker in self.workers:
            # Add additional rnd?
            self.get_wage(worker)

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

            if competitors:
                # if marking up and non-competitive
                if self.eco.goods[self.good]['price'] < self.find_average_cost()\
                        and self.markup > 0:
                    self.markup -= 0.01
                else:
                    self.markup += 0.01


    def promote(self, x=1):
        # Max number of people that can be managed is 12...
        n_structures = x
        # for i in range(len_structures)
        # have a 0.8, 1.2) management variable
        # n_structures to be a firm_wide attribute?

        # assumes 1D worker array. might not always be the case.
        prods = [worker.productivity for worker in self.workers]

        # most productive worker
        champ = self.workers[prods.index(max(prods))]
        return champ

    def pay_profits(self):
        # Profit system
        profit = self.balance
        if self.owner:
            self.owner.balance += profit

    def declare_bankruptcy(self):
        if self.balance <= -1000:
            self.open = False
            self.eco = None
            self.owner = None

    def get_marginal_product(self, worker):
        # Gets the predicted marginal product of labor if worker hired...
        # Worker object -> float
        output_added = float(worker.productivity * self.productivity)
        value_added = output_added * self.eco.goods[self.good]['price']
        return value_added








