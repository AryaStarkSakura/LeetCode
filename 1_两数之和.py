class Solution(object):
    def twoSum(self, nums, target):
        hasmap = {}
        for i,num in enumerate(nums):
            if hasmap.get(target - num) is not None:
                return [i,hasmap.get(target-num)]
            hasmap[num] = i