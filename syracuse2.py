
syracuse_dict = dict()
def syracuse(start):
    if start == 1:
        return 1

    if start in syracuse_dict:
        return syracuse_dict[start]
    
    if start % 2 == 1:
        length = 1 + syracuse(start * 3 + 1)
        syracuse_dict[start] = length
        return length
    else:
        length = 1 + syracuse(start / 2)
        syracuse_dict[start] = length
        return length


import time
start_time = time.time()
for i in range(1, 100000001):
    length = syracuse(i)
    if length > 600:
        print(i, length)

cost = time.time() - start_time
print("time_cost: {}".format(cost))