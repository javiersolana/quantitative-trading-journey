# region imports
from AlgorithmImports import *
# endregion

class CalmAsparagusCaterpillar(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2024, 1, 1)
        self.set_cash(100000)
        self.spy = self.add_equity("SPY", Resolution.MINUTE)

        self.invested = False

    def on_data(self, data: Slice):
        if not self.portfolio.invested:
            self.set_holdings("SPY", 1.0)
            self.invested = True
            self.log("Comprando SPY - Buy & Hold iniciado")

