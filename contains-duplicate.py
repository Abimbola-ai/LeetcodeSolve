class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        # """
        hashSet = set()
        hashSet.add(nums[0])
        for i in range(1,len(nums)):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
        return False
        
