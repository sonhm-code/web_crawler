import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://www.iban.com/currency-codes"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

def scrap():
  countries = []
  table = soup.find("table")
  rows = table.find_all("tr")[1:]

  for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code =items[2].text
    if name and code:
      if name != "No universal currency":
        country = {
          'name':name.capitalize(),
          'code': code
        }
        countries.append(country)
  return countries

def ask():
  countries = scrap()
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"You chose {country['name']}\nThe currency code is {country['code']}")
      ask()
  except ValueError:
    print("That wasn't a number.")
    ask()