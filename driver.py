from citizen import Citizen
from economy import Economy
from firm import Firm

import matplotlib.pyplot as plt
import pandas as pd
import pprint


def main():

    # https://factsanddetails.com/world/cat56/sub408/entry-6381.html#:~:text=The%20main%20industries%20were%20pottery,by%20hand%20in%20small%20factories.

    # These are the main industries of Ancient Rome (according to a website)
    goods = ['pottery', 'bricks', 'glass', 'metal', 'ships', 'wrought iron', 'processed fish']
    eco = Economy()

    eco.introduce_goods(goods)
    eco.introduce_citizens()
    eco.introduce_firms()
    eco.introduce_workers()

    eco.introduce_good('silk')
    eco.introduce_firm('silk')

    year = 285

    brick_ls = []
    years = []

    while year < 310:
        eco.pass_year()
        print(eco.goods['bricks'])

        brick_ls.append(eco.goods['bricks']['quantity_supplied'])
        years.append(year)
        year += 1

    plt.plot(years, brick_ls, color='red')
    plt.xlabel('Year (CE)')
    plt.ylabel('Production')
    plt.title('Growth of Imperial Brick Production 285-310')
    plt.show()


main()
