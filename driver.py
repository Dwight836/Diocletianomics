from citizen import Citizen
from economy import Economy
from firm import Firm


def main():

    # https://factsanddetails.com/world/cat56/sub408/entry-6381.html#:~:text=The%20main%20industries%20were%20pottery,by%20hand%20in%20small%20factories.

    # These are the main industries of Ancient Rome (according to a website)
    goods = ['pottery', 'bricks', 'glass', 'metal', 'ships', 'wrought iron', 'processed fish']
    eco = Economy()

    eco.introduce_goods(goods)
    eco.introduce_citizens(n=100)
    eco.introduce_firms()
    eco.introduce_workers()

    year = 0

    while year < 50:
        eco.pass_year()
        year += 1

    # I should make mu and sigma for rng class attributes instead of repeating them once again.
    # Perhaps the demand weights?


main()
