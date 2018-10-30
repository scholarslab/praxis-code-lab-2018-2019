jane = "The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
jane_cleaned= jane.split()

# find item index in list:
jane_cleaned.index('Produced')

jane_cleaned = jane_cleaned[jane_cleaned.index('Produced') :]
jane_cleaned[0:10]
# the result looks good.


# convert list to string:
jane_cleaned = " ".join(str(x) for x in jane_cleaned)
jane_cleaned[0:1000]

# Replace all instances of man with person, and wife with partner in jane_cleaned 
#Original instructions said to change "wife" to "parther", but I thought "partner" would make more sense.

jane_cleaned = jane_cleaned.replace("man", "person")
jane_cleaned = jane_cleaned.replace("wife", "partner")

print(jane_cleaned)






