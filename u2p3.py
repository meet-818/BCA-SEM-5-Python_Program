from array import *
x = array('i',[])

print("how many element you want:")
n = int(input())

for i in range(n):
    print("enter the element :",end="")
    x.append(int(input()))
print("original array",x)

flag = False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            flag = True
    if flag == False:
        break
    else:
        flag = False
print("sorted array:",x)
