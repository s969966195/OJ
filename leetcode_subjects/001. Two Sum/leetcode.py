class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            x=nums[i]
            if target-x in dict:
                return (dict[target-x],i)
            dict[x]=i
