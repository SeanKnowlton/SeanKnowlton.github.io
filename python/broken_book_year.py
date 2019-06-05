#Create a collection of texts and metadata about them. Then, print out information about those texts using a method.
# Example Data for your Collection:
#Jane Eyre, 1847
#Cane, 1923
#Wide Sargasso Sea, 1966
#Citizen: An American Lyric, 2014
#Example output you might aim for:
#Jane Eyre was published in 1847.

text = {"Jane Eyre": "1847",
	   "Cane": "1923",
       "Wide Sargasso Sea": "1966",
       "Citizen: An American Lyric": "2014"
       }
for title, date in text.items():
    print(title + " was published in " + date)
