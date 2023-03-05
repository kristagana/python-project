# Create a program that asks the user to enter their age and whether or not they have a driver's license.
# If the user is at least 18 years old and has a driver's license,
# the output should be -> You are able to drive : True
# If not, then -> You are able to drive : False

print("Enter your age:")
age = input()
print("Do you have driver's licence?")
licence = input() 
result = int(age) >= 18 and licence == str("yes")
print("You are able to drive:", result)

# # Create a program that asks the user for a password, and checks 
# # if it meets the following criteria: at least 8 characters long
# # If the password meets all of these criteria,
# #  print "Password accepted : True", otherwise print "Password accepted : False".

print("Enter your password:")
password = input()
result = len(password) >= 8
print("Password accepted:", result)

# Write a program that asks the user to enter two integers and checks if they are both even. 
# If they are, print "Both numbers are even : True", otherwise print "Both numbers are even : False".
# If at least one is even print "At least one number is even : True", else "At least one number is even : False".

print("Enter first integer:")
firstIntiger = int(input())
print("Enter second integer:")
secondInteger = int(input())
a = firstIntiger % 2
b = secondInteger % 2
result1 = a == 0 and b == 0
print("Both numbers are even:", result1)
result2 = a == 0 or b == 0
print("At least one number is even:", result2)

# Write a program that asks the user to enter a year and checks if it is a leap year. 
# A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is divisible by 400. 
# If the year is a leap year, print "Leap year : True", otherwise print "Leap year : False".

LeapYear = int(input("Enter a year: "))  
a = LeapYear % 4 == 0
b = LeapYear % 100 != 0
c = LeapYear % 400 == 0
result = a and b or c
print("Leap year:", result); 