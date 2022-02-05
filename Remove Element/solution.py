# Problem link https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length= len(nums)
        arrayIndex=0
        for i in range(0,length):
            if nums[arrayIndex] == val:
                nums.pop(arrayIndex)
                arrayIndex -=1
            arrayIndex +=1
        return len(nums)
        