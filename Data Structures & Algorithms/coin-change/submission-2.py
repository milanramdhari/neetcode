class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use DP to solve 
        # Bottom Up approach using table to store DP

        memo = [math.inf] * (amount + 1)
        memo[0] = 0

        # for every amount, go with every coins we have and check it's min coins

        for amount in range(1, amount + 1):
            for coin in coins:
                if (amount - coin) >= 0:
                    memo[amount] = min(memo[amount], 1 + memo[amount - coin])
            
        return memo[amount] if memo[amount] != math.inf else -1


        