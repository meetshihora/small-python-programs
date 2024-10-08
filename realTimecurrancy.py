from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: "))
from_currency = input("From the currency: ").upper()
to_currency = input("To the currency: ").upper()
print(f"{amount} {from_currency} is {c.convert(from_currency, to_currency, amount)} {to_currency}")