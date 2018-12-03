from bs4 import BeautifulSoup
import requests
import csv

result = requests.get('https://www.gutenberg.org/cache/epub/20321/pg20321.html')
lascasas_text = result.content
soup = BeautifulSoup(lascasas_text)

f = open('lascasasitalics.csv','w')
allitalics = soup.find_all("i")
print(allitalics, file=f)