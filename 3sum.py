# -*- coding: utf-8 -*-
"""
Created on Tue May  6 22:34:51 2025

@author: bahob
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []
        
        for i, x in enumerate(nums[:-2]):
            if i and x == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                s = x + nums[l] + nums[r]
                
                if not s:
                    answer.append([x, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1  
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l, r = l + 1, r - 1
                elif s < 0: l += 1
                else: r -= 1
                    
        return answer

# ============================
# Test etmek için aşağıyı ekle:
# ============================

if __name__ == "__main__":
    sol = Solution()
    test_input = [-1, 0, 1, 2, -1, -4]
    result = sol.threeSum(test_input)
    print("Input:", test_input)
    print("3-sum triplets:", result)
