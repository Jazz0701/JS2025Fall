#Funaction - a block of code(set of instructions)
#-runs only when it is called
# it can have arguments return output(value, data)

#syntax 
#def name_of_function():
  # execution statment

def print_name(name):
    return name

print(print_name("Jazz"))


# write a function that takes user's name and return whether the length of the name is even or odd 

# def ask_username(name = input("enter your name ?")):

#     #name = input("enter your name ?")
#     length = len(name)

#     if length%2 == 0:
#         return "Even Length"
#     else:
#         return "Odd length"
    
# print(ask_username())

#with lambda
#lambda ask_username name : "Even" if len(name)%2 ==0 else 

#Refactored - write a function that takes user's name and return whether the length of the name is even or odd 

def ask_username_refactored(name = input("enter your name ?")):
   
   return name 

def check_if_username_is_even_or_odd():

   return "even" if len(ask_username_refactored()) % 2 == 0 else "odd"

print(check_if_username_is_even_or_odd())


#function arguments a datatype
# def introduce_myself(name, course, age, gender ="Female"):
#     return f"Hello my name is {name}, {gender} and I am {age} and I am studying {course}"

# person_one = introduce_myself("Paula","python", 4 )
# person_two = introduce_myself("Jazz", "React", 5, "Male")

# print(person_one)
# print(person_two)

# WORKING WITH LIST AS A PARAMETER

fall_2025_cohort = ["Etin", "Paula", "Jazz", "Chia", "Divya"]
other_students = ["Femi", "Luckshinie", "Etin", "Paula", "Jazz"]

# step 1 : iterate through the other_students list - for loop
# step 2 : if name is in fall_2025_cohort - if/else statement

# write a function that takes 2 list and return the students that are of the present cohort
def is_a_student_of_2025(fall_students, all_students):
    for student in all_students:
        if student not in fall_students:
            continue
        else:
            print(f"{student} is a student of fall 2025 cohort")
is_a_student_of_2025(fall_2025_cohort, other_students)       

#Create a list of dictionaries called employees it should have 
#name, department, salary, return the employee with highest salary

employee = [{"name" :"Jazz", "department" :"CS", "salary" : 100}, 
            {"name" :"Lora", "department" :"BA", "salary" :120}, 
            {"name" :"Lyne", "department" :"FA", "salary" : 80} 
            ]
 
# step 1 : iterate the list - for loop
# step 2 :  get the highest salary- sorted
# step 3 : compare salary with highest salary

# def highest_salary(name, department, salary):
#     highest = dict(sorted(employee.items()))
#     for emp in employee:
        
#         if highest > salary:
#             print(f"{name} has the highest salary")
# highest_salary([{"Jazz", "CS", 100}, {"Lora", "BA", 120}, {"Lynne", "Finance", 80}])            

            
def highest_salary(employee_list):
    highest = employee_list[0]  # assume first employee has the highest salary

    for emp in employee_list:
        if emp["salary"] > highest["salary"]:
            highest = emp  # update if we find a higher salary

    print(f"{highest['name']} has the highest salary: {highest['salary']} in {highest['department']} department.")
    return highest

# Call the function
highest_salary(employee)

#write a program that find the factorial of a number

def factorial(number):
    n = 1
    for i in range(1, number+1):
        n = n*i
    return n
print(factorial(5))   

# Write a  Python function to check whether a number falls within a given range.
def func(number):


#Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

#Write a  Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5] - input list
#Unique List : [1, 2, 3, 4, 5]  - output list