class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoding: INT#strINT#str
        result = ""
        for s in strs:
            str_len = str(len(s))
            result += str_len + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        while i < len(s):
            if s[j] != "#":
                j += 1
                continue
            str_len = int(s[i:j])
            read_str = s[j+1:j+str_len+1]
            i = j = j + str_len + 1
            result.append(read_str)
        return result



