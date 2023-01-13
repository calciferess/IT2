from resource import RLIM_INFINITY, RLIMIT_AS
from secrets import choice


HALLO="HALLO"
print(HALLO.lower())

navn="kristian"
etter="sørli" 
nummer=90016670

print(navn,etter.lower(),"har telefon nummer",nummer)


dedesimaltall=float(100/1000)
deiimalltall=float(30000000)


#21

ord="spiser"


lengde=len(ord)
nyttOrd=ord[lengde-4]
print(nyttOrd)


tall1=int(input("oppgi tall 1 : "))
tall1=int(tall1)
tall2=int(input("opgi tall 2 : "))

# Program make a simple calculator






#kalkulator


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")1



