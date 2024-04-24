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

    industry_ls = []
    pop_count = []
    worker_count = []
    employee_count = []

    pop_count2 = []
    worker_count2 = []
    child_count = []

    years = []

    while year < 320:
        eco.pass_year()
        industry = 'bricks'

        industry_ls.append(eco.goods[industry]['quantity_supplied'])

        pop_count.append(len(eco.citizens))
        worker_count.append(len(eco.workforce))

        child_count.append(len([citizen for citizen in eco.citizens if citizen.age>18]))
        employee_count.append([str(firm) for firm in eco.firms if firm.good == industry][0])

        years.append(year)
        year += 1

    #pprint.pp(employee_count)

    x = years
    y = pop_count
    # y = industry_ls
    y2 = worker_count

    y3 = child_count

    #percentage = [y2/y for y2,y in zip(y, y2)]
    #print(percentage)
    percentage = [(worker_pop/total_pop) for (worker_pop, total_pop)
                  in zip(worker_count, pop_count)]

    cc_percentage = [(child_count/total_pop) for (child_count, total_pop)
                  in zip(child_count, pop_count)]

    print(pop_count)
    print()
    print(child_count)
    print()
    print(percentage)

    #plt.plot(x, percentage, color='seagreen', label='labor force participation rate')
    #plt.plot(x, cc_percentage, color='coral', label='percent under 18')

    plt.plot(x, y, color='red', label='population')
    plt.plot(x, y2, color='black', label='workforce')
    plt.plot(x, y3, color='lightblue', label='children')
    #plt.plot

    plt.xlabel('Year (CE)')
    plt.ylabel('Y')
    plt.title(f'Growth of Imperial X over Y')
    plt.grid(axis='y')
    plt.legend()
    plt.show()


main()
