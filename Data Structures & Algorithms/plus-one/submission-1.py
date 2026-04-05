class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        carry = 0
        
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if carry:
                digit += carry
                carry = 0
        
            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            digits[i] = digit
        
        if carry:
            digits.insert(0, carry)
        
        return digits
            
            



        