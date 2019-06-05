# a python program to get a list of urls to prep for webscraping

domain = "http://walshbr.com/"
pages = ['about','blog','pedagogy','projects','cv']
# make an empty list
urls = []

# appends pages to a domain to create the new urls
for page in pages:
        url = domain + page
        urls.append(url)

#method and parameter
print(urls)
