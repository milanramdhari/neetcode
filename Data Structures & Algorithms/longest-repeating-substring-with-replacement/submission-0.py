class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_len = 0
        i = 0
        res = 0

        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_len = max(max_len, freq[s[j]])

            if ((j - i + 1) - max_len > k):
                freq[s[i]] -= 1
                i += 1
            
            res = max(res, (j - i + 1))

        return res

