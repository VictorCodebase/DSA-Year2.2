'''
Mark Victor Kithinji
SCT212-0105/2022
Question 3 - Assignment 1
Approach: 
    The same approach as checking for duplicates in a sorted array. Use hash map
'''

from typing import List

class soln:
    def __init__(self, input_arr: List[int]) -> bool:
        self.arr = input_arr
        self.arr_hash = {}

    def filterRepetition(self):
        #? basecases
        if(len(self.arr) <= 0): return False

        for i in range(len(self.arr)):
            # look for a duplicate key. If none, add a new key
            if self.arr[i] in self.arr_hash:
                return True
            else:
                self.arr_hash[self.arr[i]] = True
        return False

test = soln([0, 1, 1, 3]).filterRepetition()
print(test)