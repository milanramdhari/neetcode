class Solution:

    def countSubstrings(self, s: str) -> int:
        self.res = [] 
        # count odd palindromes
        for i in range(len(s)):
            self.res.append(s[i])
            self.check(i, s)

        # count even palindromes
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                self.res.append(s[i:i+2])
                self.check2(i, i+1, s)

        return len(self.res)

    
    def check(self, i: int, s: str):
        l = i - 1
        r = i + 1

        while (l > -1 and r < len(s)):
            if s[l] != s[r]:
                break
            self.res.append(s[l:r+1])
            l -= 1
            r += 1 

    def check2(self, i: int, j : int, s: str):
        l = i - 1
        r = j + 1

        while (l > -1 and r < len(s)):
            if s[l] != s[r]:
                break

            self.res.append(s[l:r+1])
            l -= 1
            r += 1         



