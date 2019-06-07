# This is me doing the web scraping exercise
# first thing first: import 2 libraries
from bs4 import BeautifulSoup
from urllib import request

url = "https://github.com/humanitiesprogramming/scraping-corpus"

# print(url)
# print(url + "/subdomain")
html = request.urlopen(url).read()
# print(html[0:2000])

soup = BeautifulSoup(html, 'lxml')#.encode("utf-8")
print(soup.find_all('a')[0:10])

# print(soup.text[0:2000].encode("utf-8"))

# print(soup.text.replace('\n', '')[0:1000].encode("utf-8"))

#this one doesn't work
#print(soup.find_all('a').text.encode("utf-8"))

#print(soup.find_all('a')[0:10].encode("utf-8"))

# for item in soup.find_all("a")[0:10]:
#     print("======")
#     print(item.text.replace('\n',''))
