'''
Mark Victor Kithinji
SCT212-0105/2022
Question 4 - Assignment 1
Approach: 
    Loop from index 0 checking if the prev is equal to the current. then return arr(index) if there is a difference
'''

from typing import List

class soln:
    def __init__(self, input_arr: List[int]) -> int:
        self.prev = 0   
        self.arr = input_arr
    
    def checkForSingle(self):
        # input is non zero length
        if len(self.arr) <= 0: return self.arr[0]

        for i in range(1, len(self.arr), 2):
            if self.arr[i] != self.arr[i - 1]:
                if self.arr[i] != self.arr[i + 1]:
                    return self.arr[i]
                else:
                    return self.arr[i - 1]
        return self.arr[len(self.arr) - 1]

test1 = soln([5,1,1,2,2,3,3,6,6]).checkForSingle() #single starting - 5
test2 = soln([1,1,2,2,3,3,6,6,4]).checkForSingle() #single ending - 4
test3 = soln([1,1,2,3,3,6,6]).checkForSingle() #single middle - 2
print(test1)
print(test2)
print(test3)