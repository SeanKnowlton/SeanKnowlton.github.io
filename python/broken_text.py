#A book you are interested in is 457 pages long, with an average of 250 words per page. If you were to break your book into 100 equal pieces, how many words would there be in each piece? Can you write code that is flexible enough to use for different lengths?

pages = 457
word_per_page = 250
number_of_pieces = 100

each_chunk = (457 * 250)/10
print(each_chunk)
