# Step 1: save the text file as a variable Jane:
import urllib
from urllib.request import urlopen

jane = urllib.request.urlopen("https://www.gutenberg.org/files/1342/1342-0.txt").read().decode('utf-8')
jane[:1000]

jane_cleaned = jane.split("\r\n")
jane_cleaned[0:30]

# find item index in list:
jane_cleaned.index('Produced by Anonymous Volunteers')

jane_cleaned = jane_cleaned[jane_cleaned.index('Produced by Anonymous Volunteers') :]
jane_cleaned[0:10]
# the result looks good.


# convert list to string:
jane_cleaned = " ".join(str(x) for x in jane_cleaned)
jane_cleaned[0:1000]

# Replace all instances of man with person, and wife with parther in jane_cleaned (hint: check out the string method replace())

jane_cleaned = jane_cleaned.replace("man", "person")
jane_cleaned = jane_cleaned.replace("wife", "parther")