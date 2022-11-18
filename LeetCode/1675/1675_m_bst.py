from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = [num << 1 if num & 1 else num for num in nums]

        maxi = max(nums)
        res = maxi - min(nums)
        while maxi & 1 == 0:
            nums.remove(maxi)
            maxi >>= 1
            nums.append(maxi)
            maxi = max(nums)
            res = min(res, maxi - min(nums))

        return res

def test_solution():
    inp = [4,1,5,20,3]
    oup = Solution.minimumDeviation(None, inp)
    assert oup == 3

if __name__ == "__main__":
    test_solution()