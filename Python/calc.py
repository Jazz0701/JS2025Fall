# # let's create a simple calculator
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = int(input("Enter choice(1/2/3/4):"))
#     # Check if choice is one of the four options if choice in (1, 2, 3, 4):
#     if choice in (1,2,3,4):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         if choice == 1:
#             print(num1, "+", num2, "=", (num1 + num2))
#         elif choice == 2:
#             print(num1, "-", num2, "=", (num1 - num2))
#         elif choice == 3:
#             print(num1, "*", num2, "=", (num1 * num2))
#         elif choice == 4:
#             print(num1, "/", num2, "=", (num1 / num2))
#     else:
#         print("Invalid Input")

#     users_cont = input("Do you want to perform another calculation? Enter Y for yes or any other letter for No \n")

#     if users_cont.upper() == "Y":
#         continue
#     else:
#         break


#Refactored

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

import math

while True:
    choice = int(input("Enter choice(1/2/3/4/5):"))
    # Check if choice is one of the four options if choice in (1, 2, 3, 4):
    if choice in (1,2,3,4,5):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print(num1, "+", num2, "=", addition(num1, num2))
        elif choice == 2:
            print(num1, "-", num2, "=", subtraction(num1, num2))
        elif choice == 3:
            print(num1, "*", num2, "=", multiplication(num1, num2))
        elif choice == 4:
            print(num1, "/", num2, "=", division(num1, num2))
        elif choice == 5:  
            #print(num1, "^" ,num2, "=" (num1 ** num2))
             for i in range(math.floor(num2)):
                 result = 1
                 result = result * num1
        print(result)
 
    else:
        print("Invalid Input")

    users_cont = input("Do you want to perform another calculation? Enter Y for yes or any other letter for No \n")

    if users_cont.upper() == "Y":
        continue
    else:
        break