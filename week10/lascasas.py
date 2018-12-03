from bs4 import BeautifulSoup
import requests
import csv

#get the text
result = requests.get('https://www.gutenberg.org/cache/epub/20321/pg20321.html')
lascasas_text = result.content
soup = BeautifulSoup(lascasas_text)

#find all the italics
allitalics = soup.find_all("i")

#figure out how to get rid of the <i> tags themselves

#write results to csv file
with open('lascasasitalics.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(allitalics)

#this produces one long row instead of one long column

#figure out how to de-dupe the list