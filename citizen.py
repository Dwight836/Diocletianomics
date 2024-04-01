import numpy as np
import random as rnd


class Citizen:
    citizen_id = 0

    def __init__(self, set_age=None):

        if set_age is not None:
            self.age = set_age
        else:
            self.age = rnd.uniform(0, 75)

        # Sets age to a rnd variable
        self.age = rnd.uniform(0, 75)
        if set_age is not None:
            self.age = set_age

        self.productivity = np.random.default_rng().normal(1, 0.25, 1)[0]
        self.workforce = self.age >= 18
        self.alive = True
        self.job = None
        self.id = Citizen.citizen_id
        self.wage = 0

        Citizen.citizen_id += 1

    def __repr__(self):
        return f'Citizen #{self.id} | {self.age:.1f} y.o | {self.productivity:.1f}x, '

    def pass_year(self):
        # This passes one year for a citizen
        # Should I give them bank accounts? Not right now...
        self.age += 1
        self.educate()
        self.join_workforce()
        self.retire(retirement_age=60)
        self.death()

    def join_workforce(self):
        # Makes citizen join the workforce
        if self.age >= 18:
            self.workforce = True

    def reproduce(self):
        # Do something to make sure that dead / underage citizens can't reproduce
        # // This should probably be a binomial Gaussian for age...
        birth_rate = 0.08 * self.alive * (self.age >= 18) * (self.age <= 50)
        kids = rnd.choices([True, False], weights=[birth_rate, 1 - birth_rate], k=1)[0]
        return kids

    def retire(self, retirement_age):
        if self.age >= retirement_age:
            self.workforce = False
            self.productivity = 0

    def death(self):
        # This is a formula for calculating death chance. Not good...
        #death_rate = (self.age - 40) / 300
        #death_chance = rnd.uniform(0, 1)
        #self.alive = death_chance > death_rate

        self.alive = self.age < 75

    def educate(self):
        # Multiple levels of education
        if self.age > 18:
            self.job = 'student'
        self.productivity += 0.01




