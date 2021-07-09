class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        once we sort the players by age, we can apply some
        n^2 dp somewhat simply.
        """
        
        # form the list of players and then sort descending by age
        players = [(age, score) for (age, score) in zip(ages, scores)]
        players.sort(reverse=True)
        
        # make the dp array
        dp = [0] * len(players)
        
        # we need to consider the largest sum that includes/ends at each player
        for i in range(len(players)): 
            
            # we can only take scores that are higher than our current player, since sorted descending
            # means that our player[i] is younger than the current player[j]
            iscore = players[i][1]
            dp[i] = iscore
            
            # for each of the players that are older than player[i]
            for j in range(i):
                
                # if their score is greater or equal to the ith player we are considering
                if players[j][1] >= iscore: 
                    
                    # dp[i] for the ith player is the max of dp[i] and the largest sum
                    # that ended with this j player (dp[j]) + our current i players score
                    dp[i] = max(dp[i], dp[j] + iscore)
        
        # simply return the max of dp, which is the largest team score we could make
        # relative to our dp, this is the dp[i] that had the largest sum that ended with
        # the ith player when sorted by age descending
        return max(dp)