#Create a list containing containing ten words, but make a few of them variant spellings of the same word. Write a program that looks through this list and makes a copy of the original list but with standardized spellings.

words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonical_spellings = ['color','amuck','adviser','pepper']
mappings = {'colour':'color', "amok": 'amuck', 'advisor':'adviser'}

new_list = []
for word in words:
    if word in mappings:
        new_list.append(mappings[word])
else:
        new_list.append(word)

print(new_list)
