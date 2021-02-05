# This program counts the frequency of occurence of words in a given text file
import numpy as np

counts = dict()

handle = input("Enter the name of the file: ")

try:
    file = open(handle)
except:
    print("Error : Wrong file name or path")
    quit()
    
letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','x','y','z')

for line in file:
    scrape = line.rstrip()
    words  = scrape.split()
    for word in words:
        for letter in word:
            if letter.lower() in letters:
                counts[letter.lower()] = counts.get(letter, 0) + 1

a = []
for key,val in counts.items():
    a.append((val,key))
    
a.sort(reverse = True)

a_array = np.array(a)

print(a_array)





