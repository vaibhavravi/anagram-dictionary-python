# coding: utf-8
import collections

# using list comprehension to do a lot
# stripping each word of its \n end character
# converting all entries to lower case
# opening file inline
# converting the entire list to a set to remove duplicates
# converting back to list
# sorting in place ( just for convenience )
wordclean = sorted(list(set([word.strip().lower() for word in open('words3.txt','r')])))

# defining a method signature to find the signature of each word
# signature is characters of each word in alphabetical order
def signature(word):
    return "".join(sorted(word)) #joins each character in word with an empty space between

# slow anagram function
def anagram(anyword):
    return [word for word in wordclean if signature(word)==signature(anyword)]

# creating a dictionary indexed by signatures of each word
words_bysignature = collections.defaultdict(list)

for word in wordclean:
    words_bysignature[signature(word)].append(word)

# much much faster as we're just looking up the signature in the dict
def faster_anagram(anyword):
    return words_bysignature[signature(anyword)]

# creating a dict with anagrams of all the words in the english dictionary
# condition at the end to prevent words with themselves as anagrams
anagrams_all = {word: faster_anagram(word) for word in wordclean if len(faster_anagram(word)) > 1}
