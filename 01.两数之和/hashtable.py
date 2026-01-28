class Solution:
    def twoSum(self, nums: list[int], target: int) -> list  [int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

if __name__=="__main__":
    s = Solution()
    nums, target = [2, 7, 11, 15], 9
    print(s.twoSum(nums, target))  # 期望 [0, 1]