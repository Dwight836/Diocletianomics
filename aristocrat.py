from citizen import Citizen
from firm import Firm

import random as rnd


class Aristocrat(Citizen):
    def __init__(self, eco=None):
        super().__init__()

        if self.parent and not eco:
            self.eco = self.parent.eco

        self.eco = eco
        self.balance = rnd.uniform(1_000, 10_000)
        self.job = 'nobility'
        self.property = []

    def demote(self):
        # Going bankrupt / losing all property
        if self.balance < -1000:
            self.job = None
            self.property = list()

    def create_firm(self):
        # Aristocrats create firm into eco interface!
        #if self.job == 'nobility' and self.balance <= 1000 and self.eco:
        if self.balance >= 1000 and self.eco:
            investment_good = rnd.choices(list(self.eco.goods.keys()))[0]
            self.balance -= 1000
            self.eco.introduce_firm(good=investment_good, owner=self)
            self.property.append(self.eco.firms[-1])













