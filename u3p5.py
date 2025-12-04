class student:
    marks=10
    @classmethod
    def modify(cls,name):
        print("{} scored {} marks".format(name,cls.marks))
student.modify("keval")
student.modify("jay")
