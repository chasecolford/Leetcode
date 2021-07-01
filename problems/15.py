class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Since we know the target value == 0, we can iterate once and store all the target 
        compliments of nums[i] such that nums[i] + COMPLIMENT == 0. We should store this 
        in dictionary in the form {compliment: index}, so that we can quickly get the value
        for our triplet later (based on its compliment).
        
        The above is actually implicit, since the value we would need for any given nums[i] to
        make it sum to zero is simply -nums[i] (i.e., if nums[i] == 8, we need -8)
        
        Then, since we jut need to find pairs that sum to make a given compliment, we are already
        down to n^2. However, if we then simply apply the same logic from 2sum problem, 
        we can find compliements for all numbers that sum to a given target value in the first
        dictionary.
        """
        
        targets = {-num: i for i, num in enumerate(nums)}
        res = []
        indexTriplets = set()
        valueTriplets = set()
        
        # we are now just doing two sum for a list of targets
        compliments = {}
        for target in targets:
            for i, num in enumerate(nums):

                # if we have found a pair that sums to target
                if num in compliments:
                    
                    # make sure that all of the indexes are different
                    indexes = str(sorted([targets[target], compliments[num], i]))
                    values = str(sorted([-target, nums[compliments[num]], nums[i]]))
                    uniqueIndexes = len(set([targets[target], compliments[num], i])) == 3
                      
                    if (indexes not in indexTriplets) and (values not in valueTriplets) and uniqueIndexes:
                        res.append([-target, nums[compliments[num]], nums[i]])
                        indexTriplets.add(indexes)
                        valueTriplets.add(values)
                else:
                    compliments[target - num] = i
                    
            # oops, dont forget to reset this for each new target :)
            compliments.clear()
        return res

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         res = set()

#         #1. Split nums into three lists: negative numbers, positive numbers, and zeros
#         n, p, z = [], [], []
#         for num in nums:
#             if num > 0:
#                 p.append(num)
#             elif num < 0: 
#                 n.append(num)
#             else:
#                 z.append(num)

#         #2. Create a separate set for negatives and positives for O(1) look-up times
#         N, P = set(n), set(p)

#         #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
#         #   i.e. (-3, 0, 3) = 0
#         if z:
#             for num in P:
#                 if -1*num in N:
#                     res.add((-1*num, 0, num))

#         #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
#         if len(z) >= 3:
#             res.add((0,0,0))

#         #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
#         #   exists in the positive number set
#         for i in range(len(n)):
#             for j in range(i+1,len(n)):
#                 target = -1*(n[i]+n[j])
#                 if target in P:
#                     res.add(tuple(sorted([n[i],n[j],target])))

#         #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
#         #   exists in the negative number set
#         for i in range(len(p)):
#             for j in range(i+1,len(p)):
#                 target = -1*(p[i]+p[j])
#                 if target in N:
#                     res.add(tuple(sorted([p[i],p[j],target])))

#         return res