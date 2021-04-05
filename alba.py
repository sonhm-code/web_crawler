import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

request = requests.get(alba_url)
soup = BeautifulSoup(request.text,'html.parser')

super_brands = soup.find('ul',attrs={"class":"goodsBox"})
super_brands = super_brands.find_all('a',attrs={"class":"goodsBox-info"})
companies = []

for super_brand in super_brands:
  link = super_brand.find('a')
  name = super_brand.span['company']
  company = {
    'link' : link,
    'name' : name
  }
  companies.append(company)

print(companies)