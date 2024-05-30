# The state apparatus
import random as rnd


class Government:
    def __init__(self, eco=None):
        self.eco = eco

        self.tax_rate = 0.05
        self.budget = 0
        self.balance = 0

    def tax(self):
        # taxes citizens directly from balance. account system
        for citizen in self.eco.citizens:
            owed = citizen.balance * self.tax_rate
            citizen.balance -= owed
            self.balance += owed

    def defend(self):
        # Applies defense from budget, replace 1 w/ log reg type formula?
        formula = None
        self.eco.connectivity = 1
        pass

    def debt_relief(self):
        # Applies random debt relief, check for performance issues
        debtors = [citizen for citizen in self.eco.citizens if citizen.balance <= 0]

        # This could easily be an accelerated numpy array...
        for debtor in debtors:
            relieved = rnd.choices([True, False], [0.01, 0.99], k=1)[0]
            if relieved:
                debtor.balance = 0




