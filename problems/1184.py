"""
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] 
is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.
"""
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n1, n2 = 0, 0
        if start > destination:
            start, destination = destination, start
        for i in range(len(distance)):
            if i >= start and i < destination:
                n1 += distance[i]
            else:
                n2 += distance[i]
        return min(n1, n2)