class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for i in range(len(nums)):
            if nums[i] not in result:
                result[i] = 1
            else:
                result[i] += 1
        return min(result, key=result.get)