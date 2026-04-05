class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n

        def sumOfDigitSquare(num):
            result = 0
            while(num > 0):
                remainder = num % 10
                num = num // 10
                result += remainder ** 2
            return result



        while num not in seen:
            seen.add(num)
            num = sumOfDigitSquare(num)
            if num == 1:
                return True
        return False

        