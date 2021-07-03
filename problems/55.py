class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        basically the only way we cannot just walk straight to the end
        from left to right is if there are 0s in the array. If there were
        not any 0s, literally any path would lead to the end. Knowing this,
        we can make some inferences: 
        if we start at the back of the array and the square in front of us
        is not zero, we can set this square to be the new back, since being
        here is now confirmed to lead to the back.
        If at any point on our way from right to left we encounter a 0, 
        our short-term goal becomes finding a node that allows us to jump
        over this gap. If we do not find one by the time we traverse 
        the entire array, position will not be == to the starting position,
        which means we should return false.
        """
        position = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= position: position = i
        return position == 0