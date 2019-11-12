import sys

# Reverse a string

print("\nString Reverse Challenge: ")
reverse_this = input( "Enter a string to reverse: " )

char_list = list( reverse_this )
char_list.reverse()

reverse = "".join( char_list ) 

print( "\nResult: " + reverse )

# Fizz buzz

print("\nFizzbuzz Challenge: ")
start = int( input( "Enter start value: " ) )
end = int( input( "Enter end value: " ) )

numbers = [ value for value in range(start, end+1) ]

fizzbuzz = []

for number in numbers:

    if number % 15 == 0:
        fizzbuzz.append("Fizzbuzz")

    elif number % 5 == 0:
        fizzbuzz.append("Buzz")

    elif number % 3 == 0:
        fizzbuzz.append("Fizz")

    else:
        fizzbuzz.append(number)

print( "\n{}".format( fizzbuzz ) )

# Student Management System

print( "\nStudent Management" )
class Student:
    def __init__(self, name, major, hours, status):
        self.name = name
        self.major = major
        self.hours = hours
        self.status = status

    def __str__(self):
        return "%s : %s \nMajor: %s \nCompleted hours: %f" % (self.name, self.status, self.major, self.hours)

if len( sys.argv ) > 5:
    
    if sys.argv[1] == "create":
        
        new_student = Student( sys.argv[2], sys.argv[3], float( sys.argv[4] ), sys.argv[5] )
        print( new_student )