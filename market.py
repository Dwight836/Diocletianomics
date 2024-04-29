
# A market is a subset of an economy...

class Market:
    market_id = 0

    def __init__(self, region=None, eco=None):
        # This is the name of the mkt
        self.region = region
        self.eco = eco

        self.firms = []
        self.prices = {}

        Market.market_id += 1

    def set_price(self):
        # Very simple pricing formula.
        for good in self.eco.goods:
            weighed_outputs = []
            outputs = []

            for firm in self.firms:
                if firm.good == good:
                    weighed_outputs.append(firm.find_cost() * firm.inventory[good])
                    outputs.append(firm.inventory[good])

            weighted_avg_price = sum(weighed_outputs) / sum(outputs)
            self.prices[good] = weighted_avg_price










