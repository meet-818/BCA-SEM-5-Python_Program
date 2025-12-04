import math

def area_of_circle():
    radius = float(input("Enter Radius of Circle:- "))
    area = math.pi*radius**2
    print(f"Area of Circle:{area:.2f}")

def area_of_triangle():
    base = float(input("Enter Base of Triangle:- "))
    height = float(input("Enter Height of Triangle:- "))
    area = 0.5*base*height
    print(f"Area of Triangle: {area:.2f}")

def area_of_square():
    side = float(input("Enter Side of square:- "))
    area = side ** 2
    print(f"Area of Square: {area:.2f}")

def simple_interest():
    p = float(input("Enter Principal  Amount:-  ")) 
    r = float(input("Enter Rate of Interest :-  ")) 
    n = float(input("Enter year of interest :-  ")) 
    interest = (p*r*n)/100
    print(f"SI:- {interest:.2f}")

def main():
    while True:
        print("\n Menu")
        print("1.Find Area Of Circle")
        print("2.Find Area Of Triangle")
        print("3.Find Area Of Square")
        print("4.Find Simple Interest")
        print("5.Exit")
    
        choice = int(input("Enter Choice(1-5):- "))

        match choice:
            case 1:
                area_of_circle()

            case 2:
                area_of_triangle()

            case 3:
                area_of_square()

            case 4:
               simple_interest()

            case 5:
                print("Existing The Program")
                break
            
            case _:
                print("Invalid Choice")

if  __name__ == "__main__":
    main()
