class sample:
    var = 10
    @classmethod
    def new_modify(cls):
        cls.var+=1
s1=sample()
s2=sample()
print("x in s1",s1.var)
print("x in s2",s2.var)
s1.new_modify()
print("x in s1",s1.var)
print("x in s2",s2.var)
