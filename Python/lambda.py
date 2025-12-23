#lambda.py
# Lambda = an anonymous function - small
#can have many arguments but one execution 
def add_thing(x,y):
    return x,y
print(add_thing(2,6))

#lambda
adding_number = lambda x,y : x + y
print(adding_number(4,5))
#syntax 
#variable_name = lambda arguments : execution statement

number = lambda num : num
print(number(4))

even_or_odd = lambda number : "Number is even" if number % 2 == 0 else "Number is odd"
print(even_or_odd(5))

# Compare two numbers

lambda a,b : a*b

#lambda parameter : expression(lambda parameter : experssion (lambda parameter : expression))
#multiplier
multiplier = lambda n : (lambda x : x* n)
first_value = multiplier(2)
print(first_value(5))

#sort

student = [
    {"name": "Etin", "score": 50},
    {"name": "Jazz", "score": 60},
    {"name": "Leena", "score": 55}
]

sorted = sorted(students, key = lambda student : student["score"])
print(sorted)