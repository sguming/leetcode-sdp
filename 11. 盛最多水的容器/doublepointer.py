from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        while l<r:
            width=r-l
            current=width*min(height[l],height[r])
            area=max(current,area)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return area
            


if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))
    # 输出: 49