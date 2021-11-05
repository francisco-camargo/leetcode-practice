# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:35:40 2021

@author: Francisco
"""

import numpy as np


# def check_once(primes2, i):
#     for j in primes2:
#         if i % j == 0:
#             return []
#     return [i]


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 3:
#             return 0
        
#         primes = [2]
#         for i in range(3,n):
#             primes2  = np.array(primes)
#             mask = primes2 <= i**0.5
#             primes2 = list(primes2[mask])
            
#             out = check_once(primes2, i)
#             primes += out
#         return len(primes)


def remover(my_list, target):
    primes = []
    if len(my_list) == 0:
        return []
    else:
        temp = my_list.copy()
        for idx, val in enumerate(my_list):
            if val % target == 0:
                temp.pop(idx)
        return temp


class Solution:
    def countPrimes(self, n: int) -> int:

        candidates = list(range(2,n-1))
        
        candidates = remover(candidates, target)
        
        
if __name__ == '__main__':
    
    out = Solution().countPrimes(n=1)
    assert out == 0
    
    out = Solution().countPrimes(n=1)
    assert out == 0
    
    out = Solution().countPrimes(n=2)
    assert out == 0
    
    out = Solution().countPrimes(n=3)
    assert out == 1
    
    out = Solution().countPrimes(n=4)
    assert out == 2
    
    out = Solution().countPrimes(n=6)
    assert out == 3
    
    out = Solution().countPrimes(n=10)
    assert out == 4