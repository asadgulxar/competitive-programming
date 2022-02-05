# Problem Link: https://leetcode.com/problems/container-with-most-water/
class Solution:

    # Time complexity n
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        while left < right:
            area = max(area, min(height[left],height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
            


    # Time complexity n*2
    # def maxArea(self, height: List[int]) -> int:
    #     maxarea=0
    #     if len(height)<=2:
    #         return min(height[0], height[1])
            
    #     for i in range(0,len(height)-2):
    #         for j in range(i+1, len(height)):
    #             newmax=(j-i) * min(height[j], height[i])
    #             print(i,j,newmax)
    #             if newmax>maxarea:
    #                 maxarea=newmax
                    
                    
    #     return maxarea
            