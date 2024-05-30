from citizen import Citizen
from firm import Firm

import random as rnd


class Aristocrat(Citizen):
    def __init__(self):
        super().__init__()

        # placeholder balance...
        # self.balance = rnd.uniform(1_000, 10_000)
        self.balance = 1000

    def create_firm(self):
        self.balance -= 1000
        fr = Firm(good=self.job, owner=self)
        return fr







