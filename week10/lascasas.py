from bs4 import BeautifulSoup
import requests
import csv

#get the text
result = requests.get('https://www.gutenberg.org/cache/epub/20321/pg20321.html')
lascasas_text = result.content
soup = BeautifulSoup(lascasas_text)

#in theory figure out how to get rid of the preface and start at p id=“id00015” but in reality we'll just delete that

#find all the italics
allitalics = soup.find_all("i")

#write results to csv file
with open('lascasasitalics.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile,delimiter=' ')
     for italic in allitalics:
        wr.writerow(italic)

#figure out how to de-dupe the list