# -*- coding: utf-8 -*-
"""task-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRfjdXn-18AL0RPVXDCzkWYZH9PvN8WU
"""

#task-2
from queue import PriorityQueue

def function(inp, out):
    n,m = inp.readline().split()
    n = int(n)
    m = int(m)
    time_arr = []
    person_queue = PriorityQueue()
    for i in range(m):
        person_queue.put(0)

    for i in range(n):
        start, end = inp.readline().split()
        start = int(start)
        end = int(end)
        time_arr.append((start, end))

    time_arr.sort()
    # print(time_arr)

    count = 0
    for i in time_arr:
        start = i[0]
        end = i[1]
        minimum = person_queue.get()
        if(start >= minimum):
            count += 1
        else:
            person_queue.put(minimum)

        person_queue.put(end)

    print(count, file = out)

    inp.close()
    out.close()

inp = open("/content/input2.txt", "r")
out = open("/content/output2.txt", "w")
function(inp, out)