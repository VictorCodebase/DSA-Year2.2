'''
Use two variables to store the max and the val after max
'''
def max_nextMax(list):
    if len(list) <= 0:
        return None
    elif len(list) <= 1:
        return list[0]
    
    if (list[0] > list[1]):
        max = list[0]
        min = list[1]
    else:
        max = list[1]
        min = list[0]

    for val in list[2:]:
        if val > max:
            max = val
        elif val > min:
            min = val
    
    return max, min

print(max_nextMax([4, 45, 2, -30, 21, -2]))