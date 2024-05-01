import numpy as np
import random as rnd


class Citizen:
    citizen_id = 0

    def __init__(self, set_age=None, parent=None):

        # Sets age to a rnd variable
        self.age = rnd.uniform(0, 75)
        if set_age is not None:
            self.age = set_age

        self.productivity = np.random.default_rng().normal(1, 0.25, 1)[0]
        self.workforce = (self.age >= 18)
        self.alive = True
        self.job = None
        self.id = Citizen.citizen_id

        # I am going to make a rudimentary bank account system.
        self.wage = 0
        self.balance = 0
        Citizen.citizen_id += 1

        self.parent = parent

    def __repr__(self):
        return f'Citizen #{self.id} | {self.age:.1f} y.o | {self.productivity:.1f}x, {self.job} worker'

    def pass_year(self):
        # This passes one year for a citizen
        self.age += 1
        self.educate()
        self.join_workforce()
        self.retire()
        self.death()

    def join_workforce(self):
        # Makes citizen join the workforce
        if self.age >= 18:
            self.workforce = True

    def reproduce(self):
        # Citizens choose to reproduce
        # kids, Boolean
        birth_rate = 0.08 * self.alive * (self.age >= 18) * (self.age <= 50)

        #if kids:
            #return Citizen(set_age=rnd.uniform, parent=self)

        kids = rnd.choices([True, False], weights=[birth_rate, 1 - birth_rate], k=1)[0]
        survived = rnd.choices([True, False], weights=[0.7, 0.3], k=1)[0]

        if kids and survived:
            # Will eventually return baby. But not right now.
            baby = Citizen(set_age=rnd.uniform(0, 1), parent=self)

            return True

    def retire(self, retirement_age=60):
        # Citizens retire
        if self.age >= retirement_age:
            self.workforce = False
            self.job = None
            self.productivity = 0

    def death(self):
        # I do not want to work out a death formula right now.
        # Do something to increase infant mortality
        self.alive = self.age < 75

    def educate(self):
        # Multiple levels of education? Potential tiered class system
        if self.age < 18:
            self.productivity += 0.01

