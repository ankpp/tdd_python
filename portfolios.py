import operator

from functools import reduce

from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []
        self._euro_to_usd = 1.2
    
    def __convert(self, a_money, a_currency):
        if a_money.currency == a_currency:
            return a_money.amount
        return a_money.amount * self._euro_to_usd

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = reduce(operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0)
        return Money(total, currency)
