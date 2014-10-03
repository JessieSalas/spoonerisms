# Explores all non-trivial n-char substitution spoonerisms up to n=3
""" A trivial spoonerism is one where applying the spooning operation returns the 
original words
"""

from hyphen import Hyphenator
from hyphen.dictools import *

h = Hyphenator()

data = open("/home/human/data/10000_most_common_thresh5.txt","r")

output = open("all_spoons.txt", "w")

all_words = set([word.split()[0] for word in data])


def one_one(word, neighbor):
    word_spooned = neighbor[0] + word[1:] 
    neighbor_spooned = word[0] + neighbor[1:] 
    return word_spooned,neighbor_spooned

def two_two(word, neighbor):
    word_spooned = neighbor[0:2] + word[2:]
    neighbor_spooned = word[0:2] + neighbor[2:]
    return word_spooned,neighbor_spooned

def three_three(word, neighbor):
    word_spooned = neighbor[0:3] + word[3:]
    neighbor_spooned = word[0:3] + neighbor[3:]
    return word_spooned,neighbor_spooned


for word in sorted(all_words):
    for neighbor in sorted(all_words):
	if neighbor[0].lower() == word[0].lower():
	    continue #check for trivial spoonerism

        funcs = [one_one]

        for fun in funcs:

	    if len(word) < 3 or len(neighbor) < 3: 
		continue

	    p = fun(word,neighbor)

	    word_spooned = p[0]
	    neighbor_spooned = p[1]

	    if word_spooned == neighbor or word_spooned.lower() == neighbor.lower():
		continue

	    if word_spooned == neighbor + 's' or neighbor == word_spooned +'s': 
		continue

	    if word_spooned == word or word_spooned.lower() == word.lower():
		continue

	    if neighbor_spooned == neighbor or neighbor_spooned.lower() == neighbor.lower():
		continue

	    if word_spooned in all_words and neighbor_spooned in all_words: 
		output.write( word + " " + neighbor + " => " + word_spooned + " " + neighbor_spooned + " " + str(fun).split()[1]+ "  " + " \n")

print("success!")

"""
#this was bad and hard
        word_syll = h.syllables(unicode(word,"utf-8"))
        neighbor_syll = h.syllables(unicode(neighbor,"utf-8"))
	if len(word_syll) < 2:
	    break
	if len(neighbor_syll) < 2: 
	    continue #can't make syllabic substitution

	word_spooned = neighbor_syll[0]  + ''.join(word_syll[1:])
	neighbor_spooned = word_syll[0] + ''.join(neighbor_syll[1:])

	if word_spooned == neighbor or word_spooned.lower() == neighbor.lower():
	    continue

        if word_spooned == word or word_spooned.lower() == word.lower():
            continue
        if neighbor_spooned == neighbor or neighbor_spooned.lower() == neighbor.lower():
            continue
"""
