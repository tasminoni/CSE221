# -*- coding: utf-8 -*-
"""task2b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6GDsXOWp09y9CfaNI3nZ1fy4BXAt7Vf
"""

#task2b
#O(n)
inp=open("/content/input2b.txt","r")
out=open("/content/output2b.txt","w")
m = int(inp.readline())
temp1 = [int(x) for x in inp.readline().split()]
n = int(inp.readline())
temp2 = [int(x) for x in inp.readline().split()]
new_arr = [0]*(m+n)
j = 0
k = 0
s = ""
for i in range(m+n):
    if(j >= m):
        new_arr[i] = temp2[k]
        k +=1
    elif(k >= n):
        new_arr[i] = temp1[j]
        j += 1

    elif(temp1[j] < temp2[k]):
        new_arr[i] = temp1[j]
        j += 1
    else:
        new_arr[i] = temp2[k]
        k += 1

    s += str(new_arr[i]) + " "

out.write(s)
print(s)
inp.close()
out.close()