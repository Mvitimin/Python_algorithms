from typing import List
class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		
		n = len(coins)
		dp = [0] * (amount + 1)
		dp[0] = 1
		
		for c in coins:
			for i in range(c, amount + 1):
				dp[i] += dp[i - c]
		return dp[-1]
						
a = Solution()
amount = 5; coins = [1,2,5]
#amount = 10; coins = [10]			

print(a.change(amount, coins))			
