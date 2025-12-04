num = eval(input("Enter Elements in():"))
print(num)

sum = 0

n = len(num)
for i in range(n):
    sum += num[i]

print("Sum of Numbers=",sum)
print()
print("Avg of Numbers=",sum/n)
print()
print("Maximum Numbers in Tuple=", max(num))
print()
print("Minimum Numbers in Tuple=", min(num))
