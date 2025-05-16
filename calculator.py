def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b


print("Simple Calculator")
print("Choose Operation : ")
print("1. Add")
print("2. Subtract") 
print("3. Multiply") 
print("4. Division")

choice = input("Enter Choice (1,2,3,4) : ")

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

if choice == "1" :
    print("Result", add(num1,num2))
elif choice == "2" :
    print("Result" , subtract(num1,num2))
elif choice == "3" :
    print("Result", multiply(num1,num2))
elif choice == "4" :
    print("Result", division(num1,num2))
else :
    print("Invalid Input")

    
    


