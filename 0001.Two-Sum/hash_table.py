class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i in range(len(nums)):
            hash_nums[nums[i]] = i

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hash_nums and hashmap[complement] != j:
                return [j, hash_nums[complement]]