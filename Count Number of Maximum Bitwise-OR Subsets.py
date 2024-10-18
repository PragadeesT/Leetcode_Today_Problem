class Solution:
    def countMaxOrSubsets(self, nums: list[int])->int:
        a = 0
        for num in nums:
            a |= num 
        count = 0
        n = len(nums)
        def subset_or(subset):
            result = 0
            for num in subset:
                result |= num
            return result
        from itertools import combinations
        for i in range(1, n+1):
            for subset in combinations(nums, i):
                if subset_or(subset) == a:
                    count += 1
        return count
