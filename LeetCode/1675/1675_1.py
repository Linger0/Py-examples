from typing import List

class Solution:
    MAXINT = 10 ** 5

    def _operate(self, item: int):
        res = [item]
        if item % 2:  # odd
            res.append(item * 2)
            return res
        while True:
            item /= 2
            res.append(item)
            if item % 2: return res

    def _calculate(self, nums):
        n = len(nums)
        maxdev = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) > maxdev:
                    maxdev = abs(nums[i] - nums[j])
        return maxdev

    def minimumDeviation(self, nums: List[int]) -> int:
        all_nums = [self._operate(x) for x in nums]
        stack = []
        lens = [len(t) for t in all_nums]
        n = len(nums)

        mindev = Solution.MAXINT
        cur = 0
        back = False
        while True:
            if back:
                if cur == 0: break
                cur -= 1
                pop_n = stack.pop()
                if pop_n < lens[cur] - 1:
                    stack.append(pop_n + 1)
                    cur += 1
                    back = False
            else:
                if cur == n:
                    mindev = min(mindev, self._calculate([all_nums[i][stack[i]] for i in range(n)]))
                    back = True
                else:
                    stack.append(0)
                    cur += 1
        return mindev

def test_all():
    solution = Solution()
    inp = 8
    oup = solution._operate(inp)
    assert oup == [8, 4, 2, 1]
    inp = 1
    oup = solution._operate(inp)
    assert oup == [1, 2]

    inp = [1, 8, 3, 5]
    # exp = [[1, 2], [2, 1], [3, 6], [4, 2, 1]]
    exp = 7
    oup = solution._calculate(inp)
    assert oup == exp

    inp = [1, 2, 3, 4]
    oup = solution.minimumDeviation(inp)
    assert oup == 1

if __name__ == '__main__':
    test_all()
