from citizen import Citizen
from firm import Firm

import random as rnd


class Aristocrat(Citizen):
    def __init__(self, eco=None):
        super().__init__()

        self.eco = eco
        if self.parent and not eco:
            self.eco = self.parent.eco

        self.balance = rnd.uniform(1_000, 10_000)
        self.job = 'nobility'
        self.entrepreneur = False
        self.property = []

    def demote_noble(self):
        # Going bankrupt / losing all property
        if self.balance < -1000:
            self.job = None
            self.property = list()
            #print('Noble Demoted')

    def create_firm(self):
        # Aristocrats create firm into eco interface!
        if self.balance >= 1000 and self.eco:
            investment_eco_goods = self.eco.goods
            goods = list(investment_eco_goods.keys())
            investment_good = rnd.choices(goods)[0]
            self.balance -= 1000
            self.eco.introduce_firm(good=investment_good, owner=self)
            self.property.append(self.eco.firms[-1])
            self.entrepreneur = True

    def pass_fiscal_year(self):
        # 1% chance to create firms
        if rnd.choices([True, False], [0.01, 0.99])[0]:
            self.create_firm()

        # Cancels unsuccessful entrepreneurship if no open firms
        if self.property:
            if True not in [prop.open for prop in self.property if type(Firm)]:
                self.entrepreneur = False
















