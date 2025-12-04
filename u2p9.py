max = lambda x,y : x if x>y else y
a,b = [int(n) for n in input("enter two Number:").split(',')]
print("Bigger number = ",max(a,b))
