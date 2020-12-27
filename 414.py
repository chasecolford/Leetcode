"""
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).
"""#NOTE: THIRD DISTINCT -> PROBLEM INTRO SHOULD SAY THIS

def thirdMax(nums) -> int:
    smallies = [float('-inf'), float('-inf'), float('-inf')]
    for num in nums:
        if num not in smallies:
            if num > smallies[0]: smallies = [num, smallies[0], smallies[1]]
            elif num > smallies[1]: smallies = [smallies[0], num, smallies[1]]
            elif num > smallies[2]: smallies = [smallies[0], smallies[1], num]
    return max(nums) if float('-inf') in smallies else smallies[-1]

# expcted 1
print(thirdMax([3, 2, 1]))

# expected 2
print(thirdMax([1, 2]))

# expected 3
print(thirdMax([2, 2, 3, 1]))