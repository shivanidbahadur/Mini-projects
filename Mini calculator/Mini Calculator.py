# MINI CALCULATOR
loop=0

print("Enter two numbers")

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

while loop==0:
     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")


     op=input("Choose the operation:").lower()
     if op == "addition":
        print(a,"+",b,"=",a+b)

     elif op == "subtraction":
        print(a,"-",b,"=",a-b)

     elif op == "multiplication":
        print(a,"*",b,"=",a*b)

     elif op == "division":
        if b == 0:
            print("Invalid: Division by zero")
        else:
            print(f"Quotient={a/b:.2f}")
            print("Remainder=",a%b)
     elif op == "exit":
            break
     else:
        print("Invalid operation. Please choose a valid one.")

     op=input("Do you want to perform another operation? (yes/no)").lower()
     if op == "no":
         break
     change=input("Do you want to change the number? (yes/no)").lower()
     if change == "yes":
         a=float(input("Enter first number:"))
         b=float(input("Enter second number:"))
print("THANK YOU!!")





