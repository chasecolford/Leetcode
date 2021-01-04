"""
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""

#NOTE: both strings need to have the same characters and the same frequency counts for distinct patterns of them
#NOTE: Example
"""
The string "aabbcccd" has [2, 2, 3, 1] relative character frequency, as does the string "bbddaaac".

This means we can compare the set of the two strings, and also compare the counts of each of the relative frequencies of the patterns
Python makes this easy with Counter:
    where counter(string) returns a dictionary of the counts of each distinct char in the string. Then, we can either sort this and compare,
    or take the counter of this counter object. i.e., Counter(Counter(str1))
    The counter of the counter is smart becasue we can compare the hash without sorting, since we only care that the patterns line up in count,'
    which can be expresed in an arbitrary order
"""
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

# def closeStrings(word1: str, word2: str) -> bool:
#     print(Counter(word1).values())
#     print(Counter(Counter(word1).values()))
#     print(Counter(word2).values())
#     print(Counter(Counter(word2).values()))
#     return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

# closeStrings(word1 = "cabbba", word2 = "abbccc")
# closeStrings(word1 = "cabbba", word2 = "aabbss")