'''
Mark Victor Kithinji
SCT212-0105/2022
Question 1 - Assignment 1
Approach: 
    Use a hashmap to keep track of unique elements, then use an index to keep track of where the unique nums end
'''

from typing import List #? Just for types

class soln:
    def __init__(self, input_arr: List[int]) -> List[int]:
        self.arr = input_arr
        self.unique_hash = {}
        self.unique_index = 0

    def removeDup(self):
        #? handling basecases
        if(len(self.arr)) == 0:
            print("hello")
            return self.arr
        for val in self.arr:
            #? Check if val is in hash, only then update hashmap and overwrite the val in unique index
            if val not in self.unique_hash:
                self.arr[self.unique_index] = val
                self.unique_hash[val] = True
                self.unique_index += 1
        print(self.unique_index)
    
test = soln([0, 0, 0, 2]).removeDup()

