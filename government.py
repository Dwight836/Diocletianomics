# The state apparatus
import random as rnd


class Government:
    def __init__(self, eco=None):
        self.eco = eco

        self.tax_rate = 0.05
        self.budget = 0
        self.balance = 0

    def tax(self):
        # taxes citizens directly from balance. account system?
        for citizen in self.eco.citizens:
            citizen.balance *= (1-self.tax_rate)
            self.balance += (citizen.balance * self.tax_rate)

    def defend(self):
        # Applies defense from budget, replace 1 w/ log reg type formula?
        formula = None
        self.eco.connectivity = 1
        pass

    def debt_relief(self):
        # Applies random debt relief, check for performance issues
        debtors = [citizen for citizen in self.eco.citizens if citizen.balance <= 0]
        for debtor in debtors:
            if False:
                debtor.balance = 0




