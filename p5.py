list1=[1,2,3,4,5]
list2=[5,4,7,8,9]
for item in list1:
    if item in list2:
        print(item,"Common Element")

for item in list1:
    if item not in list2:
        print(item,"Are non Common Element")
        print(item,"Are Common Element")
        
