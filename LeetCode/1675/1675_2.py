from typing import List

class Solution:
    r"""Multiply the minimum number or divide the maximum one.
    Prefer to divide the maximum number.
    """
    def minimumDeviation(self, nums: List[int]):
        nlen = len(nums)
        nidx = nlen - 1
        qsort(nums)

        while True:
            curmin = nums[nidx] - nums[0]
            if nums[nidx] % 2 == 0:  # even
                temp = nums[nidx] / 2
                if nums[nidx-1] - temp <= curmin:
                    nums[nidx] = temp
                    sort_one(nums, nlen, forward=False)
                    continue

            # left
            if nums[0] % 2:  # odd
                nums[0] *= 2
                if nums[0] - nums[1] >= curmin:
                    break
                sort_one(nums, nlen)
            else:
                break

        return int(curmin)


def sort_one(arr, lenth, forward=True):
    ran = range(lenth - 1)
    if not forward:
        ran = reversed(ran)
    for i in ran:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            break

def qsort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partiIndex = parti(arr, left, right)
        qsort(arr, left, partiIndex - 1)
        qsort(arr, partiIndex + 1, right)
    return arr

def parti(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        i += 1
    arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
    return index - 1

def test():
    solution = Solution()
    # inp = [399,908,648,357,693,502,331,649,596,698]
    # oup = solution.minimumDeviation(inp)
    print(oup)

if __name__ == "__main__":
    test()