class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            fuel = 0
            for station in range(n):
                fuel += gas[(start + station) % n]
                # print(start, (start + station) % n)
                fuel -= cost[(start + station) % n]
                if fuel < 0: break
            else: return start
            continue
        return -1