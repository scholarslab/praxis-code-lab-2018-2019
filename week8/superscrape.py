from bs4 import BeautifulSoup
import requests

result = requests.get('http://maybe.scholarslab.org/blog/')
slab_blog = result.content
soup = BeautifulSoup(slab_blog)

blogtitles = soup.find_all("div",class_="blog-item__title")
for title in blogtitles:
    for link in title.find_all('a'):
        print(link.get('href'))