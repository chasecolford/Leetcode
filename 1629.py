class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        longest, key = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            d, k = (releaseTimes[i] - releaseTimes[i-1]), keysPressed[i]
            if longest <= d:
                if longest == d:
                    key = max(key, k)
                else:
                    longest, key = d, k
                
        return key