class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("how many student:"))
i=0
while(i<n):
    s=student()
    name=input("Enter Name:")
    s.setname(name)
    marks=int(input("Enter Marks:"))
    s.setmarks(marks)
    i +=1
