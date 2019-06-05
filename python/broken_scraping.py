#We want to scrape a number of pages from my blog. In order to do that, we’ll need a list of several URLs to point our Python program to. We know the name of each page we are interested in, and we know the top-level domain. Make a new list consisting of all the URLs we want by combining the two. domain = ‘http://walshbr.com/’ pages = [‘about’,’blog’,’pedagogy’,’projects’,’cv’]

domain = "https://walshbr.gov/"
pages = ["about",'blog','pedagogy','projects', 'cv']
urls = []

for page in pages:
	url = domain + page
	urls.append(url)

print(urls)
