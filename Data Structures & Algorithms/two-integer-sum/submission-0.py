class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashSet = {}
        for i in range(len(nums)):
            if target - nums[i] in hashSet:
                return sorted([hashSet[target-nums[i]], i])
            else: 
                hashSet[nums[i]] = i