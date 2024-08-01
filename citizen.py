import numpy as np
import random as rnd


class Citizen:
    citizen_id = 0

    def __init__(self, set_age=None, parent=None):

        self.id = Citizen.citizen_id
        Citizen.citizen_id += 1

        self.age = rnd.uniform(0, 75)
        if set_age is not None:
            self.age = set_age

        # should be 40% less in cases...
        self.productivity = np.random.default_rng().normal(1, 0.25, 1)[0]
        self.workforce = (self.age >= 18)
        self.alive = True
        self.job = None

        self.wage = 0
        self.balance = 0

        self.parent = parent
        if self.parent:
            if self.parent.job == 'nobility':
                self.job = 'nobility'
        self.children = []

    def __repr__(self):
        return f'Citizen {self.id} | {self.age:.1f} y.o | {self.productivity:.1f}x, {self.job} worker'

    def pass_year(self):
        # This passes one year for a citizen
        self.age += 1
        self.educate()
        self.join_workforce()

        self.retire()
        self.death()
        self.inherit()

    def join_workforce(self):
        # Makes citizen join the workforce
        if self.age >= 18:
            self.workforce = True

    def reproduce(self):
        # Citizens choose to reproduce
        birth_rate = 0.08 * self.alive * (self.age >= 18) * (self.age <= 50)
        kids = rnd.choices([True, False], weights=[birth_rate, 1 - birth_rate], k=1)[0]
        survived = rnd.choices([True, False], weights=[0.7, 0.3], k=1)[0]

        # If citizen chose to have a kid, and it survived Y1
        if kids and survived:
            baby = Citizen(set_age=rnd.uniform(0, 1), parent=self)
            self.children.append(baby)
            return baby

    def retire(self, retirement_age=60):
        # Citizens retire
        if self.age >= retirement_age:
            self.workforce = False
            self.job = None
            self.productivity = 0

    def death(self):
        # Rudimentary death system
        weights = None
        # weights = [500, self.age**2]
        living = rnd.choices([True, False], weights=weights, k=1)[0]
        self.alive = self.age < 75

    def educate(self):
        # Multiple levels of education? Potential tiered class system
        if self.age < 18:
            self.productivity += 0.01

    def inherit(self, tax_rate=0):
        # Citizens receive the assets of their parents upon death.
        if not self.alive:
            # If dead, loops through child list
            if self.children:
                estate = self.balance
                estate -= (estate * tax_rate)
                for child in self.children:
                    child.balance += (estate / len(self.children))

    def promote(self):
        # Citizens become aristocrats
        if self.balance >= 1000:
            self.job = 'nobility'

    def demote(self):
        # Citizens become unfree...
        if self.balance <= -1000:
            self.job = None
            # self.freedom = False









