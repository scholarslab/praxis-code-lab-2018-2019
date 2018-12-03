from bs4 import BeautifulSoup
import requests
import csv

#get the text
result = requests.get('https://www.gutenberg.org/cache/epub/20321/pg20321.html')
lascasas_text = result.content
soup = BeautifulSoup(lascasas_text)

#figure out how to get rid of the preface and start at p id=“id00015”

#find all the italics
allitalics = soup.find_all("i")

#figure out how to get rid of the <i> tags themselves

#write results to csv file
with open('lascasasitalics.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile,delimiter=' ')
     #should we add quoting=csv.QUOTE_ALL?
     for italic in allitalics:
        wr.writerow(italic)

#figure out how to de-dupe the list