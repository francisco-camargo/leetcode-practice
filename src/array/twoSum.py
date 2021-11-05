# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:01:28 2021

@author: Francisco
"""

from typing import List


def find_index(array, value, nth_instance):
    return [i for i, n in enumerate(array) if n == value][nth_instance]
    
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:

# =============================================================================
#         # O(n^2)
#         for idx, val in enumerate(nums):
#             for idxb, valb in enumerate(nums):
#                 if idx != idxb and val + valb == target:
#                     valid_index = [idx, idxb]
# =============================================================================
        
# =============================================================================
#         if len(nums) == 2:
#             if nums[0] != nums[1]:
#                 valid_index = [ nums.index(nums[0]), nums.index(nums[1]) ]
#             else:
#                 idx0 = find_index(nums, nums[0], 0)
#                 idx1 = find_index(nums, nums[0], 1)
#                 valid_index = [idx0, idx1]
# 
#         else:
# 
#             dic = {}
#             for idx, val in enumerate(nums):
#                 if val not in dic.keys():
#                     dic[val] = {}
#                     dic[val]['loc'] = [nums.index(val)]
#                     dic[val]['count'] = 1
#                     dic[val]['compliment'] = target - val
#                     # dic[val]['single'] = True
#                     # if val == dic[val]['compliment']:
#                         # dic[val]['equal'] = True
#                     # else:
#                         # dic[val]['equal'] = False
#                 else:
#                     dic[val]['loc'] += [find_index(nums, val, 1)]
#                     dic[val]['count'] += 1
#                     # dic[val]['single'] = False
#                     
#             for key, item in dic.items():
#                 if dic[key]['count'] == 2 and 2*key == target:
#                     valid_index = dic[key]['loc']
#                     break
#                 elif dic[key]['compliment'] in dic.keys():
#                     if dic[key]['count'] == 1 and 2*key == target:
#                         pass
#                     else:
#                         valid_index = dic[key]['loc'] + dic[dic[key]['compliment']]['loc']
#                         break
#                     
#         return sorted(valid_index)
# =============================================================================

    

if __name__ == '__main__':
    
    nums = [2,7,11,15]; target = 9
    out = Solution().twoSum(nums, target)
    assert out == [0,1]
    
    nums = [2,3,4]; target = 6
    out = Solution().twoSum(nums, target)
    assert out == [0,2]
    
    nums = [3,3]; target = 6
    out = Solution().twoSum(nums, target)
    assert out == [0,1]
    
    nums = [3, 2, 3]; target = 6
    out = Solution().twoSum(nums, target)
    assert out == [0,2]
    
    nums = [-3, 4, 3, 90]; target = 0
    out = Solution().twoSum(nums, target)
    assert out == [0,2]
    
    nums = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]; target = 11
    out = Solution().twoSum(nums, target)
    assert out == [5,11]
    
    nums = [2,4,11,3]; target = 6
    out = Solution().twoSum(nums, target)
    assert out == [0,1]
    
    nums = [3,2,4]; target = 6
    out = Solution().twoSum(nums, target)
    assert out == [1,2]