x = {}
print("How Many Players?")
n = int(input())
for i in range(n):
    print("Enter Player Name:")
    k = input()
    print("Enter Runs:")
    v = int(input())
    x.update({k:v})
print(x)

print("Enter Player Name:")
name = input()

runs = x.get(name,-1)
if (runs == -1):
    print("Players Not Found")
else:
        print("{} Made {} Runs".format(name,runs))
        
