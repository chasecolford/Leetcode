from collections import Counter
def findLeastNumOfUniqueInts(arr, k):
    counts = Counter(arr).most_common()
    for i in range(k-1, -1, -1):
        if counts[-1][1] == 1: counts.pop()
        else:
            v, c = counts[-1]
            counts[-1] = (v, c-1)
    return len(counts)

print(findLeastNumOfUniqueInts([2,1,1,3,3,3], 3))