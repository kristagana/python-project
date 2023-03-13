# Write a program that takes a user input (an integer) 
# and determines whether it is positive, negative, or zero.

number = int(input("Please enter number: "))
if number == 0:
    print("Entered number", str(number), "is zero")
elif number < 0:
    print("Entered number", str(number), "is negative")
else:
    print("Entered number", str(number), "is positive")

# Write a program that prints out the numbers from 1 to 100.
#  But for multiples of three, print "Fizz" instead of the number #  and for multiples of five, print "Buzz". 
# For numbers that are multiples of both three and five, print "FizzBuzz".

for i in range(1,100):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print(i)

# Other option (from Monday session):

# for i in range(1,100):
# printnumber = True
# if i % 3 == 0:
#     print("Fizz", end="")
#     printnumber = False

# if i % 5 == 0:
#     print("Buzz", end="")
#     printnumber = False

# if printnumber:
#     print(i)
# else:
#     print()

# Write a program that takes an integer as input and prints out all the factors of that integer.

num = int(input("Please enter number: ")) 
for i in range (1, num):
    if(num % i == 0):
        print(i)
print(num)

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
        print(first * second) 
    elif operation == "/":
        print(first / second)
    elif operation == "+":
        print(first + second)
    elif operation == "-":
        print(first - second)
    else:
        print("Operation provided isn't valid, please,try again")
        break
 # Other option (from Monday session):
 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# while True:
#     operation = input("Select operation *,/,+.- or %: ")
#     if operation == "*":
#         result = num1 * num2
#     elif operation == "/":
#         result = num1 / num2
#     elif operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     else:
#         print("Operation provided isn't valid, please,try again")  
#         continue
#     print("Result is " + str(result))
#     break

# Write a program that takes an integer as input and prints out whether that integer is prime or not.
# Check on Monday

enterednumber = int(input("Please enter number: "))
prime = True

for i in range (2,enterednumber):
    if(enterednumber % i == 0):
        prime = False

if enterednumber > 1 and prime:
    print("Number is prime")
else:
    print("Number is not prime")