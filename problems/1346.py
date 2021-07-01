class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # O(n): if we have seen num * 2 previously, then we return true
        # or if num is even and we have seen num / 2, then return true as well
        # else, we just return false
        cache = set()
        for num in arr: 
            if num in cache: return True
            else:   
                cache.add(num*2)
                if num % 2 == 0:
                    cache.add(num // 2)
        return False