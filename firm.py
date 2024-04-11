

class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None):
        # Each firm produces a good
        self.good = good
        self.eco = eco
        self.workers = []
        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def __repr__(self):
        return f'{self.good} firm, employing {len(self.workers)} workers'

    def produce(self):
        # if a firm is IN an economy
        if self.eco:
            prod = sum([worker.productivity for worker in self.workers])

            # if firm produces a good that is demanded by the economy
            if self.good in self.eco.goods.keys():
                self.eco.goods[self.good]['quantity_supplied'] += prod

    def hire_worker(self, worker):
        # Worker is a citizen object

        self.workers.append(worker)
        worker.job = self.good

    def set_price(self):
        # Adds market price (since these firms are currently monopolies
        # How does this happen?
        pass

    def set_wage(self):
        # Sets a wage for every worker at that factory (I will make it 1)
        for worker in self.workers:
            wage = 1
            worker.wage = wage

    def pay_wage(self):
        # Should this even be a function?
        pass

# There needs to be a way to hire all the citizens in an economy
# Should they be randomly assigned to firm ids? Or competitive labor market...?
# I think I will be randomly assigning them...

# Costs and their implications. Firm specific?
# labor costs should be wage... maybe cost of materials and labor?
# materials should be determined through the good...
# material price should be specific to the economy (later the market...)
