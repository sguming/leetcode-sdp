from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            # 第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])

                    # 第二个数去重
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # 第三个数去重
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))