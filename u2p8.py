print("Positional Argument:")
def attach(s1,s2):
    s3=s1+s2
    print("Total String  " +s3)

attach("New","York")
print(" ")
#Keywords args
print("Kewords Arguments:")
def grocery(item,price):
    print("item = %s" % item)
    print("price=%.2f"% price)
grocery(item = 'Suger',price = 50.75)
grocery(price = 88.00,item = 'oil')
print(" ")
#default args
print("default argument")
def grocery(item,price = 40.00):
          print("item = %s" %item)
          print("price = %2f" %price)
grocery(item =  'Suger',price = 50.75)
grocery(item = 'tea', price = 63.00 )
print(" ")

#or program 8
def adder(*args):
    sum = 0
    for n in args:
        sum = sum+n
        print("sum=",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
print(" ")
