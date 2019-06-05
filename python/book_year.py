#define a collection
literature = {'Jane Eyre': '1847',
              'Cane': '1923',
              'Wide Sargasso Sea': '1966',
              'Citizen: an American Lyric': '2014'
              }

for title, date in literature.items():
        print(title + " was published in " + date)


# dictionary.items says "take this thing, give it an order, and give me the pairs"
