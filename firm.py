

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

    def set_wage(self):
        # Sets a wage for each worker
        for worker in self.workers:
            wage = worker.productivity
            worker.wage = wage

    def pay_wage(self):
        # Pays wages
        for worker in self.workers:
            worker.balance += worker.wage

    def set_price(self):
        # Adds market price...
        pass


