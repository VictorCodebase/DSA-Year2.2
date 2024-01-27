'''
Mark Victor Kithinji
SCT212-0105/2022
Question 2 - Assignment 1
Approach: 
    Use K to only flip the part needing to be fliped using 2 pointers?
'''

from typing import List

class soln:
    def __init__(self, k: int, input_arr: List[int]):
        # self.index = 0
        self.k = k
        self.arr = input_arr
        self.first_side = []
    
    def rotate(self):
        #? basecases
        if(len(self.arr)) == 0:
            return self.arr
        if(self.k <= 0): return self.arr

        # for val in range(0, self.k):
        #     temp = self.arr[self.index]
        #     self.arr[self.index] = self.arr[self.k - self.index]
        #     self.arr[self.k - self.index] = temp
        #     self.index += 1
        for val in range(0, self.k):
            temp = self.arr[val]
            self.arr[val] = self.arr[self.k - val]
            self.arr[self.k - val] = temp
        return self.arr
            
    
ans = soln(2, [1,2,3,4]).rotate()
print (ans)