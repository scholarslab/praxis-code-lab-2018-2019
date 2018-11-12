from bs4 import BeautifulSoup
import requests

result = requests.get('http://maybe.scholarslab.org/blog/')
slab_blog = result.content
soup = BeautifulSoup(slab_blog)

f = open('blogpostlinks.txt','w')
with open('blogpostlinks.txt','w') as file:
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