import requests
from bs4 import BeautifulSoup
import re

url = 'https://comics.gocollect.com/guide/view/126360'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

gradeList = soup.find_all('div', class_='col-3 col-xl-2')
priceList = soup.find_all('div', class_='col-5 col-xl-6 pr-xl-0 text-right')

index = 0
for g in gradeList:
    gradeRegex = re.findall(r'\d+\.\d+', g.text)
    if len(gradeRegex) > 0:
        if gradeRegex[0] == '9.0':
            grade = gradeRegex[0]
            gradeIndex = index
            break
    index += 1

priceElement = priceList[gradeIndex].text
priceRegex = re.findall(r'\$(\d+(?:[\.,]\d+)*)', priceElement)
price = priceRegex[0]

print(grade)
print(price)
