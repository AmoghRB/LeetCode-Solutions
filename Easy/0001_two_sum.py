# Problem 1. Two Sum
# Easy
# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=nb5f1cwc
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
