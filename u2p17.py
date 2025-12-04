student = ["Kasak","Maahi","Meet"]
marks = [84,80,79]

z = zip(student,marks)
d = dict(z)
print("{:15s} -- {:15s}".format("Student","Marks"))
for i in d:
    print("{:15s} -- {:5d}".format(i,d[i]))
    
