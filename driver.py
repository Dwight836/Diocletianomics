from citizen import Citizen
from economy import Economy
from firm import Firm

import matplotlib.pyplot as plt
import pandas as pd
import pprint
import seaborn as sns


def main():

    # https://factsanddetails.com/world/cat56/sub408/entry-6381.html#:~:text=The%20main%20industries%20were%20pottery,by%20hand%20in%20small%20factories.

    # These are the main industries of Ancient Rome (according to a website)
    goods = ['pottery', 'bricks', 'glass', 'metal', 'ships', 'wrought iron', 'processed fish']
    eco = Economy()

    eco.introduce_goods(goods)
    eco.introduce_citizens(n=1000)
    eco.introduce_firms()
    eco.introduce_workers()

    eco.introduce_good('silk')
    eco.introduce_firm('silk')

    year = 285

    while year < 320:
        eco.pass_year()
        year += 1

    sns.set()
    y1 = [citizen.balance for citizen in eco.citizens if citizen.age > 18]
    y2 = [citizen.age for citizen in eco.citizens if citizen.age > 18]
    y3 = [citizen.wage for citizen in eco.citizens if citizen.age > 18]
    plt.scatter(x=y2, y=y1, c=y3, marker='.')
    plt.colorbar()
    plt.show()


main()

