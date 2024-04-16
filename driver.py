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

    year = 300

    ls = []
    while year < 325:
        eco.pass_year()
        ls.append(eco.goods)
        year += 1

    y = [eco.goods[good]['quantity_supplied'] for good in eco.goods.keys()]
    x = eco.goods.keys()
    #plt.bar(x, y)
    #plt.show()

    #pprint.pp(ls)
    industry = 'bricks'
    industry_list = [dc[industry]['quantity_supplied'] for dc in ls]
    pprint.pp(industry_list)



    #pprint.pp(eco.__dict__)
    #for firm in eco.firms:
    #ls = [firm.inventory for firm in eco.firms]
    #print(ls)
    #key = 'quantity_supplied'

    #char_ls = [ls[good]]

    #df_timeline = pd.DataFrame(ls)
    #print(df_timeline.head())

    #df_timeline.to_csv('output.csv')





main()
