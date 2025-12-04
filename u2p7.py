def modify(list):
    list.append(9)
    print(list,id(list))

list = [1,2,3,4,5,6,7,8,]
modify(list)
print(list,id(list))
