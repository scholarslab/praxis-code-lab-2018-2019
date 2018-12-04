# The code below is a simple example for demonstrating several analysis of the text from web scraping.
# packages used in this assignment:
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.book import *
from nltk.corpus import stopwords
import matplotlib
import matplotlib.pyplot as plt
# web scrap the text of the book "The Secret Adversary" (by Agatha Christie in 1922) on Gutenberg.org website:
result = requests.get('https://www.gutenberg.org/files/1155/1155-0.txt')
Christie_TSA = result.text
# text data cleanning: removing stop words and punctuations:
stop_words = set(stopwords.words('english')) 
tokens = nltk.word_tokenize(Christie_TSA)
tokens = [word.lower() for word in tokens if word.isalpha()]
tokens = [word for word in tokens if not word in stop_words]
fdist1 = FreqDist(tokens)
# ANALYSIS 1: Long words exploration:
# find the top 50 words whose lengths larger than 5 characters and frequencies larger than 40 and print them out:
csw = [w for w in tokens if len(w) > 5 and fdist1[w] > 40]
cswtop50 = FreqDist(csw).most_common(50)
print(cswtop50)
# ANALYSIS 2: Words exploration:
# create a array of the top 50 most frequent words in this text and print it out:
most_50 = fdist1.most_common(50)
print(fdist1.most_common(50))
# ANALYSIS 3: Plot making:
# generate and save the plot of the most frequent 50 words:
fig = plt.figure(figsize=(20,10))
fdist1.plot(50)
fig.savefig('word_frequency.png', dpi = 300)

# create a html with this word frequency plot:
f = open('week10_website.html','w')
message = """<html>
<head></head>
<body>
<img src="word_frequency.png" alt="Word frequency top 50" style="width:2000px;height:1000px;" align="left">
<figcaption caption align="middle"><h1>Top 50 frequent words of The Secret Adversary by Agatha Christie</h1></figcaption>
</body>
</html>"""
f.write(message)
f.close()
