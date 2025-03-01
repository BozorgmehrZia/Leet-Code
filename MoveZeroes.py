# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]

def swap(nums):
    # for j in range(len(nums)):
    #     for i in range(len(nums)):
    #         if nums[i] == 0 and i < len(nums) - 1:
    #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1

    return nums


if __name__ == '__main__':
    print(swap([0, 1, 0, 3, 12]))
    print(swap([0]))
    print(swap([1, 2, 3]))
