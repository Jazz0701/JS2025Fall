# #print()

# #Data Type
# #for/while loop
# #lists
# #if/elif/else
# #functions
# #classes

# #This is a comment

# #print
# myName = "Jazz"


# print('Hello World!', end ="\n")
# print(myName)
# print(123)

# print("Jazz", end ="@")
# print('sozentech.com')
# #end -parameter \n


# print("Hello" , "Jazz" , "I" , "Love" , "Python" , sep ="-")

# #variables - Container/bag/storage for data values
# #variable_name = data_value
# my_name = "Jazz"

# my_fav_number = 1
# my_fav_number = my_fav_number + 7
# print(my_fav_number)

# #datatype
# #string - "Jazz", "4" , "1.65"
# # float - 1.0, 3.14, 3.5
# # int - 1, -1, 0, 1
# #boolean - True or False
# #list - a collection of data types, ordered, repeated, mutable(changeable)
# #      - ["Femi" , 1, 1.5, True, [], [3, "Jazz"] ]
# # dictionary - a collection of data types, unordered, mutable, key
# # -mydict = {
# #  key: value,
# #  name: "Jazz
# #  city: "Calgary"
# #  }
# #student_1 = {name : "Jazz" , age : 5, fav_color:"all colors"}

# #tuple - collection, ordered, immutable - location = (1, 343, 2.566)
# #benefit of tuple - when you want fixed data

# #set - collection, no duplicates, mutable, unordered
# # name_of_student = {"Leena", "Etin", "Pooja","Etin"}
# #Set for unique items
# name_of_student = {"Leena", "Etin", "Pooja","Etin"}
# print(name_of_student)

# #loop - repeating something over and over again until a condition is met
# #for loop
# #while loop

# #for loop - execute a set of statement, once for each item in a list or tuple or set

# #while loop - as long as a condition is true, execute this statement

# # for loop
# # for this items:
#      # do this(set of statements)
# my_students = ['Divya', 'Ola', 'chigoze', 'Paula']

# for student in my_students:
#      print(student, "is a great student")
#      #print("{}is a great student".format(student))
#      #print(f"")

# # create a list of numbers - print the number + 2
# my_list =[1,2, 3, 4, 5]

# for list in my_list:
#      print(list+2, "is a number of list + 2")

# #range - built-in function, returns a sequence of number, 
# # start by default at 0,
# # increase by 1, 
# # stops before the specified number
# #range(6) - 0,1,2,3,4,5
# #range(start, stop, step)
# #range(start,stop)
# #range(stop)
# #range(1,5) - 1,2,3,4
# #range(1, 10, 2) - 1, 3, 5, 7, 9

# for i in range(5, 20, 4):
#      print(i)

# #class task
# # Q1. Write a for loop that prints from 2 to 11.
# for i in range(2,12,1):
#      print("2 to 11 of", i)  

# # Q2. Write a for loop that prints 2, 5, 8, 11.
# for i in range(2,12,3 ):
#      print(i)

# # Q3. Write a for loop that prints 1, 2, 3, 5, 8, 13, 21.
# a, b = 1, 2
# for i in range(7):  # we want 7 numbers
#     print(a)
#     a= b
#     b= a + b
    
# # get index - enumerate()
# my_students2 =[" Pri", "lie", "happy", "chi"]
# for index,item in enumerate(my_students2):
#      print("at position", index, "is", item)

# # use a for loop for to create even number 0/2

# #while loop

# #pre-condition - initialization
# #while condition :
#   #execution statement
# #aftercondition

# #print 1 to 5  

# number = 1
# while number <=5:  #True
#      print(number) # do this
#      number+=1

# #ask your for an input, keep asking until the input is 0

# #while number!=0:
#  #  print(int(input("Please enter a number")))
    
# #print("end here")    
  

# number2 = 5
# while number2 > 0:
#      print("greater than 0", number2)
#      number2 -=1

# else :
#      print(" you have reached else", number2)

# for i in range(3):
#      print(i)
# else:
#      print("you have reached else")   

# # continue and break
# num = 0
# while num < 8 :
#      num+=1
#      if(num == 3):break
#      print(num)
     
# #task 1:2
# #Ask the user for two values and append the two values to a list and print the list.

# a = int(input("Please enter first number -"))
# b = int(input("Please enter second number -"))
# mylistsum = []
# mylistsum.append(a)
# mylistsum.append(b)
# print(mylistsum)


# #task 2:
# # Ask the user for a value and keep asking until the value is between 10 and 50. use a while loop.
# #user_input = int(input("Enter a value :"))

# #while user_input >= 10 and user_input <= 50 :
#  #    print(user_input)


# #list
# empty_list = []
# print(empty_list)
# empty_list.append("Ola")
# print(empty_list)

# #index in list
# random_list =["Divya", "Sreyasi", "Fatemah", 23, ['1', '2', [12, 14, 15], "3"], "Tham", True, "Rupinder" ,1 ]
# #positive index - left to right starts from 0
# #negative index - right to left starts from -1

# print(random_list[4][2][2])
# print(random_list[-5][-2][-1])

# #join 2 list

# list_a = ['a', 'b', 'c']
# list_b = [1,2,3]
# list_c = list_a + list_b
# print(list_c)

# #slicing
# #wit_num[start:end:step] includes the start, exclude the end
# wit_num = [0,1,2,3,4,5,6,7,8,9,10]
# print(wit_num[1:6])
# print(wit_num[1:6:2])

# random_list2 =["Divya", "Sreyasi", "Fatemah", 23, ['1', '2', [12, 14, 15], "3"], "Tham", True, "Rupinder" ,1,False,[12.4,67] ]
# #print(random_list2[2:8:4])
# print(random_list2[-2:10])
# #print(random_list2[-2:10]) #empty list as slicing go fro big to small negative number
# #print(random_list2[-10:-2:-2]) #again error empty list as it doesn't understand neg(-2) steps
# print(random_list2[-10:-2:2])
# print(random_list2[:-2:2]) # takes list from beg when beg not given
# print(random_list2[2::]) #if the end sn't specified it will include it
# print(random_list2[::2])


#if else
#if(condition is true):
 #    do this
#elif:
#do this   

#function - block of code, only execute when you call it, you can have parameters, returns a results

#syntax
#def func_name(par1, par2):
 #    execution statement

# def addition(val1, val2):
#      result = val1+ val2
#      return result

# result = addition(1,2)     

# A police officer is looking for a criminal 
# who named Sam, who is a 34 year old female.
# Find the criminal from the suspectList

suspectList = [{
  'name': 'Sam',
  'sex': 'Male',
  'age': 21
}, {
  'name': 'John',
  'sex': 'Male',
  'age': 25
}, {
  'name': 'Sandra',
  'sex': 'Female',
  'age': 22
}, {
  'name': 'Sam',
  'sex': 'Male',
  'age': 34
}, {
  'name': 'Paula',
  'sex': 'Female',
  'age': 29
}, {
  'name': 'Sam',
  'sex': 'Female',
  'age': 34
}]

for suspect in suspectList:
     if suspect['name'] == 'Sam' and suspect['sex'] == 'Female' and suspect['age'] == 34:
          print("Criminal Sam Found", suspect )
     else:
          print("keep searching")     


# Write an if statement that prints “>” if first number is larger than second number, “<” if first number is smaller than second number,
#  == if they are equal.

fn = 10
sn = 3

if fn > sn :
     print(">")

elif fn < sn :
     print(">")

elif fn == sn:
     print("=")     



# There is a list of integers [2, 6, 1, 5, 9, 4, 10, 3, 8, 7].
# Write a program where it takes an integer input(grater than 0) from the user 
# and prints out all the numbers in the list which are smaller than the user input.
# i.e. If the user typed an integer 5, the output should be 2 1 4 3. (separate line or same line, but in the same order from the list)
New_list = [2, 6, 1, 5, 9, 4, 10, 3, 8, 7]
user_number = int(input(" Enter a number :"))
for number in New_list:
     if number < user_number :
          print("This number is smaller than user input", number)
    


# There is a list of integers [2, 6, 1, 5, 9, 4, 10, 3, 8, 7].
# Write a program where it prints out the sum of the elements inside the list.
sum = 0
list_2 = [2, 6, 1, 5, 9, 4, 10, 3, 8, 7]
for number in list_2:
     sum = sum + number 

print(" the sum of list is" , sum)

# When a year is given, write a program that prints 1 if the year is leap year, and prints 0 otherwise.
# You can tell that it is a leap year, when the year is multiple of 4, AND is not multiple of 100 or is multiple of 400.
# For example, 2012 is a multiple of 4, and not a multiple of 100, so it is a leap year.
# 1900 is a multiple of 100, and not a multiple of 400, so it is not a leap year.
# 2000 is a multiple of 400, so it is a leap year.

# 1 < year < 4000

# Sample Input A: 2000
# Sample Output A: 1

# Sample Input B: 1999
# Sample Output B: 0

yearA = int(input("Enter a year :"))

if yearA % 4 == 0 and yearA % 100 != 0 or yearA % 400 !=0 :
     print("It is a leap year")
else:
     print("Not a leap year")

# You’re teaching math in high school and you need a program to enter students’ grades based on their exam score.
#  Write a program that takes a score of student’s math exam, and prints a proper grade based on the following rule:
# * type(score) = int
# A: 90~100
# B: 80~89
# C: 70~79
# D: 60~69
# F: ~59

score = int(input("Enter score :"))

if score >= 90 and score <= 100 :
     print("Grade : A")

elif score >= 89 and score <= 80:
     print("Grade : B")

elif score >= 79 and score <= 70:
     print("Grade : C")     

elif score >= 69 and score <= 60:
     print("Grade : D")     

elif score <= 59:
     print("Grade : E")     