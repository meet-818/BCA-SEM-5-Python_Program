class student:
    def __init__(self,nm='.',ag=15,m=0):
        self.name=nm
        self.age=ag
        self.marks=m
    def display(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s=student("Nisha",18,46)
s.display()
s1=student("shama")
s1.display()
