words = ['color','color','colour',
        'amok','amok','amuck',
        'adviser','advisor','adviser',
        'pepper']

canonical_spellings = ['color','amuck','adviser','pepper']
mappings = {"colour" : "color", "amok" : "amuck", "advisor" : "adviser"}


# make an empty list
new_list = []

# Loop over the list of words
for word in words:
        if word in mappings:
            # if a word is mispelled do x
            # correct the spelling using the mappings dictionary
            corrected_word = mappings[word]
            # add that corrected_word
            new_list.append(corrected_word)
        else:
            # if a word is correct do y
            new_list.append(word)

print(new_list)
