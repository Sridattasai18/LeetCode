class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        m = k
        while m in num_set:
            m += k
        return m