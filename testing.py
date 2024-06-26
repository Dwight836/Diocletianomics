from citizen import Citizen
from economy import Economy

from market import Market
from firm import Firm


def main():

    e = Economy()
    e.introduce_goods(['grain', 'beer'])

    m = Market(region='Egypt', eco=e)

    f1 = Firm(good='grain', eco=e)
    f2 = Firm(good='grain', eco=e)
    f3 = Firm(good='beer', eco=e)

    e.firms.append(f1)
    e.firms.append(f2)
    e.firms.append(f3)

    e.introduce_citizens(n=100)
    e.introduce_workers()

    for _ in range(25):
        e.pass_year()
        print(e.goods['grain']['price'])
        # print(f1.balance, f2.balance)


main()

