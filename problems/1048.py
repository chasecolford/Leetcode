class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                goal = word[:i] + word[i + 1:]

                if goal in dp:
                    dp[word] = max(dp[goal] + 1, dp[word])
                    res = max(res, dp[word])

        return res