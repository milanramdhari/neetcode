class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
            
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        def find_comb(index, curr_str):
            if index == len(digits):
                res.append(curr_str)
                return
    
            for ch in phone[digits[index]]:
                find_comb(index + 1, curr_str + ch)

        
        find_comb(0, "")
        return res
