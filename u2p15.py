emp = ((10,"MAHI",4000),(20,"KASAK",50000),(30,"MEET",2000))

print(sorted(emp))
print()
print(sorted (emp,reverse = True))
print()
print(sorted (emp,key = lambda x: x[1]))
print()
print(sorted (emp,key = lambda x:x[2]))
