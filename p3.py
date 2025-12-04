element=[10,20,30,40,15]
print("element before Modifying")
print(element)
x=bytearray(element)
x[0]=88
x[1]=99
print("Element After Modifying")
for i in x:print(i)
