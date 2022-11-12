## importing required libraries
import requests 
from bs4 import BeautifulSoup
from csv import writer
import pandas


website = 'https://www.cartrade.com/new-car-launches/p-1/'

r = requests.get(website)
print(r.status_code)
soup = BeautifulSoup(r.content,'html.parser')

## Results
results = soup.find_all('li',{'itemtype' : "https://schema.org/Article"})
print(len(results))


c = []
for name in results:  
  a = name.find('a').get_text().split()
#   print(a) 
  c.append(a) 
#   if a != None:
#     b = a.get_text()
#     # print(b)
#     if b != None:
#        c.append(b)
print(c)
print("This are the names of all models")
for i in c:
    for j in i:
        k = 