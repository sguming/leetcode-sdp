class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,x in enumerate(nums):
            for j in range(i+1,len(nums)):
                if x + nums[j] == target:
                    return [i,j]


if __name__ == "__main__":
    s = Solution()
    nums, target = [2, 7, 11, 15], 9
    print(s.twoSum(nums, target))  # 期望 [0, 1]