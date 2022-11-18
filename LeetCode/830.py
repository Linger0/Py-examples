from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        last = " "
        cnt = 0
        out = []
        for i, char in enumerate(s):
            if char == last:
                cnt += 1
            else:
                if cnt >= 3:
                    out.append([i - cnt, i - 1])
                cnt = 1
                last = char
        return out

def test_solution():
    answer = Solution()
    s = "abbxxxxzzy"
    out = answer.largeGroupPositions(s)
    assert out == [[3, 6]]
