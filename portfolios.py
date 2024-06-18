import operator

from functools import reduce

from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._euro_to_usd = 1.2
    
    def __convert(self, a_money, a_currency):
        exchange_rates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if a_money.currency == a_currency:
            return a_money.amount
        key = f"{a_money.currency}->{a_currency}"
        return a_money.amount * exchange_rates[key]

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0)
        return Money(total, currency)
