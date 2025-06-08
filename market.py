
# A market is a subset of an economy...

class Market:
    market_id = 0

    def __init__(self, region=None, eco=None):
        # This is the name of the mkt
        self.region = region
        self.eco = eco
        self.firms = []
        self.prices = {}
        self.product = 0
        self.connections = {}

        # Important factor for compounding
        self.growth_margin = 0.05

        Market.market_id += 1

    def expand_product(self):
        # Local market booming
        self.product *= (1 + self.growth_margin)

    def contract_product(self):
        # Local market contracting (surplus)
        self.product *= (1 - self.growth_margin)

    def get_market_prices(self):
        pass

    def connect(self, other, strength=1):
        # Creating transportation links with other markets
        self.connections[other.region] = strength

    def trade(self, other):
        # Conducting trade with linked markets
        pass

