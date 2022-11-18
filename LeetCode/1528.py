"""
class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        sNew = list(s)
        for i, idx in enumerate(indices):
            sNew[idx] = s[i]
        return ''.join(sNew)
"""

class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        return ''.join([dict(zip(indices, s))[i] for i in range(len(s))])

if __name__ == "__main__":
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    sOut = Solution.restoreString(None, s, indices)
    print(sOut)