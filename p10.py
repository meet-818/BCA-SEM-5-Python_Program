group1=[1,2,3,4,5]
search=int (input ("Enter Element to search:"))
for element in group1:
    if search==element:
        print("Element Found in the list",search)
        break
    else:
        print(search,"Element not found")
        
