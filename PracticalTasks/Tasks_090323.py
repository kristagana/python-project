# Write a program that takes a user input (an integer) 
# and determines whether it is positive, negative, or zero.

number = int(input("Please enter number: "))
if number == 0:
    print("Entered number", str(number), "is zero");
elif number < 0:
    print("Entered number", str(number), "is negative");
else:
    print("Entered number", str(number), "is positive");

# Write a program that prints out the numbers from 1 to 100.
#  But for multiples of three, print "Fizz" instead of the number #  and for multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

for i in range(1,16):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print(i)

# Write a program that takes an integer as input and prints out all the factors of that integer.

num = int(input("Please enter number: "))
factorial = 1 
for i in range (1, num + 1):
    factorial *= i
print("Factorial for entered number", str(num), "is ", str(factorial))

# Create calculator
# Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). If the operation
# provided does not match one of these, the program should print 
# "Operation provided isn't valid, please,try again" - in this case, the program should
# ask for the operation to be provided again

while True:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    operation = input("Select operation *,/,+.- or %: ")
    if operation == "*":
        print(int(first * second))
    elif operation == "/":
        print(int(first / second))
    elif operation == "+":
        print(int(first + second))
    elif operation == "-":
        print(int(first - second))
    else:
        print("Operation provided isn't valid, please,try again")      
# Question: Where I need to put break to stop program above?

# Write a program that takes an integer as input and prints out whether that integer is prime or not.
# Check on Monday
    










