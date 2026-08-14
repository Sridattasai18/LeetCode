class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                c = collections.Counter(s[i: j])
                if not any(v > 2 for v in c.values()): res = max(res, j - i)
        return res