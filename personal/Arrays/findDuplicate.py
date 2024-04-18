import math
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 1 or not nums:
            return None

        numsDict = {} #empty dict
        # repeated: List[int] = [0] * len(nums)
        repeated =""
        duplicates = 0

        for num in nums:
            if num in numsDict:
                repeated +=( str(num)+"|")
                duplicates += 1
            else:
                numsDict[num] = 1

        soln: List[int] = [0] * duplicates
        index = 0
        val_str = ""
        for val in repeated:
            if val == "|":
                soln[index] = int(val_str)
                val_str = ""
                index += 1
            else:
                val_str += val

        return soln
        
        
    def printArray(self, array):
        if array is None or not array:
            print("No duplicates found")
            return[-1]
        for value in array:
            print(value)

soln: Solution = Solution()

duplicates = soln.findDuplicates([4,3,2,7,8,2,3,1])
soln.printArray(duplicates)