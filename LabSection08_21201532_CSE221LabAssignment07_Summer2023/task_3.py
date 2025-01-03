# -*- coding: utf-8 -*-
"""task-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U2HFt-LhWr0sngw-3vMIK71qaU0OH0AM
"""

#task-3
def find(r, friend_circle):
    if(friend_circle[r] != r):
        friend_circle[r] = find(friend_circle[r], friend_circle) #path compression

    return friend_circle[r]

def funtion(inp, out):
    person, n = inp.readline().split()
    person = int(person)
    n = int(n)
    friend_circle = [0] * (person + 1)
    friend_circle_size = [1] * (person + 1)
    for i in range(len(friend_circle)):
        friend_circle[i] = i
    for i in range(n):
        a,b = [int(x) for x in inp.readline().split()]
        parent_a = find(a, friend_circle)
        parent_b = find(b, friend_circle)
        if(parent_a != parent_b):
            friend_circle[parent_b] = friend_circle[parent_a]
            friend_circle_size[parent_a] += friend_circle_size[parent_b]


        print(friend_circle_size[parent_a], file = out)

    inp.close()
    out.close()

inp = open("/content/input3.txt", "r")
out = open("/content/output3.txt", "w")
funtion(inp, out)