from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums=SortedList(num<<1 if num&1 else num for num in nums)

        ans=nums[-1]-nums[0]
        while not nums[-1]&1:
            nums.add(nums.pop()>>1)
            ans=min(ans, nums[-1]-nums[0])

        return ans

def test_solution():
    inp = [1, 2, 3, 4]
    oup = Solution.minimumDeviation(None, inp)
    assert oup == 1