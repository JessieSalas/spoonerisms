Spoonerisms
==========

This simple algorithm generates valid nontrivial n-char spoonerisms as defined here, up to and including n=3
----------------

Definitions
===========

**I define an n-char spoonerism in this scope as the result of swapping the first n characters of two word inputs word1 and word2.**

*E.g. "big dad" => "dig bad"*

  1-char spoonerism

 
 *"milky suds" => "sulky mids"*
 
 2-char spoonerism
 
**A spoonerism is valid if swapping the first n characters of word1 and word2 results in two valid English words (which I examine by checking for membership in the input dictionary)**

*E.g. "Funny Punk" => "Punny Funk" VALID*

     *"Green Money" => "Mreen Goney" INVALID*

**A spoonerism is trivial if the swap results in two words identical to the input words.**


*E.g. "Bad bunny" => "bad Bunny" TRIVIAL*

*(Here we made a 1-char substitution which resulted in "b" swapping with "B", which made no change to the words)*

Use
===
Given an input corpus (dictionary), running   python spoon.py  generates n-char spoonerisms.
More thorough semantic validation techniques will be added soon!
all_spoons.txt is the output of spoons.py
------
