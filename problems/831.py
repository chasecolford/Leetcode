class Solution:
    def maskPII(self, s: str) -> str:
        # thanks to lee's solution for cleaning up most of the busy work
        at = s.find('@')
        if at >= 0:
            return (s[0] + "*" * 5 + s[at - 1:]).lower()
        s = "".join(i for i in s if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(s) - 10] + "***-***-" + s[-4:]