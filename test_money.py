import unittest

from money import Money
from portfolios import Portfolio


class TestMoney(unittest.TestCase):

    def test_multiplication(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = ten_euros.times(2)
        self.assertEqual(ten_euros.times(2), twenty_euros)

    def test_division(self):
        original_amount = Money(4002, "KRW")
        amount_after_division = original_amount.divide(4)
        expected_money = Money(1000.5, "KRW")
        self.assertEqual(expected_money, amount_after_division)

    def test_addition(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        fifteen_dollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteen_dollars, portfolio.evaluate("USD"))

    def test_add_dollars_to_euros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_result = Money(17, "USD")
        actual_resut = portfolio.evaluate("USD")
        self.assertEqual(expected_result, actual_resut, f"{expected_result} != {actual_resut}")

    def test_addition_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        elevenhundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, elevenhundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate("KRW")
        self.assertEqual(expected_value, actual_value, f"{expected_value} != {actual_value}")

    def test_addition_with_multiple_exchange_rates_missing(self):
        one_dollar = Money(1, "USD")
        one_euro = Money(1, "EUR")
        one_won = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(
            Exception,
            "Missing exchange rate(s):[USD->Kalganid,EUR->Kalganid,KRW->Kalganid]",
        ):
            portfolio.evaluate("Kalganid")



if __name__ == "__main__":
    unittest.main()