class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = 0
        i3 = 0
        i5 = 0
        dp = []
        dp.append(1)
        for i in range(n):
            tmp = min(2*dp[i2], 3*dp[i3], 5*dp[i5])
            dp.append(tmp)
            if tmp == 2*dp[i2]:
                i2 += 1
            elif tmp == 3*dp[i3]:
                i3 += 1
            else:
                i5 += 1
        return dp[-1]

s = Solution()
import pdb
pdb.set_trace()
t = s.nthUglyNumber(10)
