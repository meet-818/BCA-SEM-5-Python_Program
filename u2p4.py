from array import *
x=array('i',[])
print("How Many Element ?",end="")
n=int(input())
for i in range(n):
    print("Enter Element:",end="")
    x.append(int(input()))
print("Original Array",x)
print("Enter The Element To Search:")
s=int(input())
try:
    pos=x.index(s)
    print("found at Position:",pos+1)
except ValueError:
    print("not found in the array")
    
