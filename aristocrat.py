from citizen import Citizen
from firm import Firm

import random as rnd


class Aristocrat(Citizen):
    def __init__(self, eco=None):
        super().__init__()

        self.eco = None
        self.balance = rnd.uniform(1_000, 10_000)
        self.job = 'nobility'
        self.property = []

    def demote(self):
        # Sets
        if self.balance < -1000:
            self.job = None
            self.property = list()

    def create_firm(self):
        # Aristocrats create firm into eco interface!
        if self.job == 'nobility' and self.balance <= 1000 and self.eco:
            good = [self.eco['goods'].keys()][0]
            self.eco.introduce_firm(good=good, eco=self.eco)
            self.balance -= 1000













