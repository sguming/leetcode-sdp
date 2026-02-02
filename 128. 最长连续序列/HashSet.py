from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:
            if x - 1 not in s:          # x 是某个连续段的起点
                cur = x
                length = 1
                while cur + 1 in s:
                    cur += 1
                    length += 1
                best = max(best, length)

        return best
if __name__ == "__main__":
    s = Solution()
    nums = [100,4,200,1,3,2]
    print(s.longestConsecutive(nums))
    # 输出: 4