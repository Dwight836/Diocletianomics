import copy

from citizen import Citizen
from economy import Economy
from aristocrat import Aristocrat

from market import Market
from firm import Firm

import matplotlib.pyplot as plt
import seaborn as sns
import random as rnd
from pprint import pprint

from collections import Counter


def main():

    e = Economy()
    e.introduce_goods(['grain', 'beer'])

    m = Market(region='Egypt', eco=e)

    f1 = Firm(good='grain', eco=e)
    f2 = Firm(good='grain', eco=e)
    f4 = Firm(good='grain', eco=e)

    f3 = Firm(good='beer', eco=e)

    e.firms.append(f1)
    e.firms.append(f2)
    e.firms.append(f4)

    e.firms.append(f3)

    e.introduce_citizens(n=1000)
    e.introduce_workers()

    x1 = list()
    x2 = list()
    x3 = list()

    c1 = list()
    c2 = list()
    c3 = list()

    for _ in range(25):
        e.pass_year()
        # print(e.goods['grain']['price'])
        #x1.append(f1.balance)
        #x2.append(f2.balance)
        #x3.append(f3.balance)

        #c1.append(f1.markup)
        #c2.append(f2.markup)
        #c3.append(f3.markup)

        #c1.append(f1.balance)
        #c2.append(f2.balance)
        #c3.append(f3.balance)

        c1.append(f1.income)
        c2.append(f2.income)
        c3.append(f3.income)

        x1.append(f1.markup)
        x2.append(f2.markup)
        x3.append(f3.markup)

    cmap = 'Purples'

    # Find a way to flip firm balance to color and markup as Y axis.
    sns.set()

    plt.plot(range(len(x1)), x1, label=f'f1 {f1.productivity:.2f}', c='red')
    plt.plot(range(len(x2)), x2, label=f'f2 {f2.productivity:.2f}', c='orange')
    plt.plot(range(len(x3)), x3, label=f'f3 {f2.productivity:.2f}', c='purple')

    plt.scatter(range(len(x1)), x1, c=c1, marker='o', cmap=cmap)
    plt.scatter(range(len(x2)), x2, c=c2, marker='o', cmap=cmap)
    plt.scatter(range(len(x3)), x3, c=c3, marker='o', cmap=cmap)

    plt.xlabel('years')
    plt.ylabel('firm markup')
    plt.colorbar(label='Income')
    plt.legend()
    plt.show()


main()

def main2():

    e = Economy()
    e.introduce_citizens()
    e.employ_workers()
    e.introduce_goods(['grain', 'beer'])
    e.introduce_firms()


def maine():

    e = Economy()
    e.simulate(n_citizens=1000)
    #ecos = [eco.goods['glass']['price'] for eco in Economy.history]
    #pops = [len(eco.citizens) for eco in Economy.history]
    #pprint(ecos)
    #print(pops)

    #a = Aristocrat(eco=e)
    #print(e.goods.keys())
    firms = [firm for firm in e.firms]
    # Most firms don't have workers...


# maine()


