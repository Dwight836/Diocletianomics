

class Firm:
    firm_id = 0
    
    def __init__(self, good=None, eco=None):
        # Each firm produces a good
        self.good = good
        self.eco = eco
        self.workers = []
        self.firm_id = Firm.firm_id
        Firm.firm_id += 1

    def produce(self):

        # if a firm is IN an economy
        if self.eco:
            prod = sum([worker.productivity for worker in self.workers])
            #print('prod', prod)

            if self.good in self.eco.goods_demanded.keys():
                self.eco.goods_supplied[self.good] += prod

    def hire_worker(self, worker):
        # Worker is a citizen object
        self.workers.append(worker)
        worker.job = self.good

# There needs to be a way to hire all the citizens in an economy
# Should they be randomly assigned to firm ids? Or competitive labor market...?
# I think I will be randomly assigning them...