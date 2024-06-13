from citizen import Citizen
from firm import Firm

import random as rnd


class Aristocrat(Citizen):
    def __init__(self):
        super().__init__()

        # self.balance = rnd.uniform(1_000, 10_000) // placeholder
        self.balance = 1000
        self.job = 'nobility'

    def demote(self):
        if self.balance < -1000:
            self.job = None

    def create_firm(self):
        # This is for performance. Adjusted as needed.
        if self.job == 'nobility' and self.balance <= 1000:
            pass













