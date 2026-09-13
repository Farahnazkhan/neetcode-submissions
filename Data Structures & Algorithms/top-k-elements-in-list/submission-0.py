class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsLen = len(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        for (n, c) in count.items():
            bucket[c].append(n)

        res = []
        if k <= 0:
            return res

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

