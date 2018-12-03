from bs4 import BeautifulSoup
import requests

result = requests.get('https://www.gutenberg.org/cache/epub/20321/pg20321.html')
lascasas_text = result.content
soup = BeautifulSoup(lascasas_text)

f = open('blogpostlinks.txt','w')
firstblogtitles = soup.find_all("div",class_="blog-item__title")
for title in firstblogtitles:
    for link in title.find_all('a'):
        initialresults = link.get('href')
        print(initialresults, file=f)
previousblogtitles = soup.find_all("ul",class_="page-previous_posts")
for title in previousblogtitles:
    for link in title.find_all('a'):
        furtherresults = link.get('href')
        print(furtherresults, file=f)