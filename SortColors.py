# Given an array with n objects colored red, white or blue, a fucntion to sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1 and 2 to represent the color red, white and blue respectively.
# Note: without using library's in-built sort functions.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = nums.count(0)
        two = one + nums.count(1)
        for i in range(len(nums)):
            if nums[i] == 2:
                if 0 <= i < one:
                    index = nums.index(0, i)
                    tmp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = tmp
                if one <= i < two:
                    index = nums.index(1, i)
                    tmp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = tmp
            if nums[i] == 1:
                if 0 <= i < one:
                    index = nums.index(0, i)
                    tmp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = tmp
                if two <= i:
                    index = nums.index(0, i)
                    tmp = nums[i]
                    nums[i] = nums[index]
                    nums[index] = tmp
