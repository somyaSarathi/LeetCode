class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        
        for i in range( 2, len(nums) ):
            nums[i] = max( nums[i-2]+nums[i], nums[i-1] )

        return nums[-1]