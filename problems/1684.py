import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys


def countConsistentStrings(allowed, words):
    good = 0
    for word in words:
        if all(1 if c in allowed else 0 for c in word): good += 1
    return good

#epected 2
print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))

#expected 4
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))