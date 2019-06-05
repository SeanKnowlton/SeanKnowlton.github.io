#gonna get the libraries that we need to do this
import nltk
from bs4 import BeautifulSoup
from urllib import request

#store the url we are using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

#this will get the html from a url using a urlopener found in the request method bulit into the urllib we imported
html = request.urlopen(url).read()

#took the url and turned into a soup object
soup = BeautifulSoup(html, 'lxml')
our_text = soup.text
links = soup.find_all('a')[0:10]


#print(our_text[0:2000])
# replace the line breaks with spaces
#print(soup.encode("utf-8").text.replace('\n', ' '))

links_html = soup.select('td.content a')
this_link = links_html[0]

#print(this_link['href'])
urls = []
#take each link and make a new list w/ processed urls
for link in links_html:
        to_append = link["href"].replace('blob/', '')
        urls.append("https://raw.githubusercontent.com/" + to_append)
print(urls)
