"""
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray 
of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.
"""
def checkSubarraySum(nums, k):
    modDict = {0:-1}
    cumSumModK = 0
    for i, n in enumerate(nums):
        if k: cumSumModK = (cumSumModK + n) % k
        else: cumSumModK += n
        if cumSumModK not in modDict: modDict[cumSumModK] = i
        else: 
            if i - modDict[cumSumModK] >= 2: return True
    return False

# expected: True
print(checkSubarraySum([23, 2, 4, 6, 7], 6))

# expected: True
print(checkSubarraySum([23, 2, 6, 4, 7], 6))