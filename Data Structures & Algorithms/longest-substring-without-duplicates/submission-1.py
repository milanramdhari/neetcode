class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        res = 1
        seen = set()
        i = 0 
        j = 0

        while i <= j:
            if j == len(s):
                break
            
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                res = max(res, len(seen))
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
                seen.add(s[j])
                j += 1

        return res


        