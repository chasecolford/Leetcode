class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """ o(n): two pass: l->r, r->l
        store dp array where dp[i] == [x,y,z];
        where x,y,z are the shortest distances from colors[i] to
        colors 1,2,3 respectively.
        """
        n = len(colors)
        dp = [[float('inf'),float('inf'),float('inf')] for _ in range(n)]
        for i in range(n):
            for j in range(3): dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            dp[i][colors[i]-1] = 0
        last = [float('inf'),float('inf'),float('inf')]
        for i in range(n-1,-1,-1):
            for x in range(3): last[x] += 1
            last[colors[i]-1] = 0
            for j in range(3): dp[i][j] = min(dp[i][j], last[j])
        res = []
        for i,c in queries:
            res.append(dp[i][c-1] if dp[i][c-1] != float('inf') else -1)
        return res