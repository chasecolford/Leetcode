import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys


def getSumAbsoluteDifferences(nums):
    res, left, right, n = [], 0, sum(nums), len(nums)
    for i, num in enumerate(nums):
        res.append(right - (n - i) * num + i * num - left)
        right -= num
        left += num
    return res

#expected [24,15,13,15,21]
print(getSumAbsoluteDifferences([1,4,6,8,10]))