import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

maximum_page = 3 # user customized range
request = requests.get(alba_url)
soup = BeautifulSoup(request.text,'html.parser')

super_brands = soup.find('ul',attrs={"class":"goodsBox"})
super_brands = super_brands.find_all('a',attrs={"class":"goodsBox-info"})
companies = []

for super_brand in super_brands:
  link = super_brand.get('href')
  name = super_brand.find('span',attrs={'class':'company'}).string
  company = {
    'link' : f'{alba_url}{link}',
    'name' : name
  }
  companies.append(company)
  
customized_companies = companies[0:maximum_page]

for company in customized_companies:
  company_url = company.get('link')
  print(requests.get(company_url).status_code)
  