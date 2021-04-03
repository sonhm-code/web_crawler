from scrap import ask, scrap
from babel.numbers import format_currency

countries = scrap()
print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")
ask()

