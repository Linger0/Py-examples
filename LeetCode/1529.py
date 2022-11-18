class Solution:
    def minFlips(self, target: str) -> int:
        crt, rtn = '0', 0
        for ch in target:
            if crt != ch:
                crt = ch
                rtn += 1
        return rtn

if __name__ == "__main__":
    target = "10111"
    rst = Solution.minFlips(None, target)
    print(rst)