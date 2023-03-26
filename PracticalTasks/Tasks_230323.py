# Task 1: Write a function that takes two parameters (a and b) and returns their sum.

# def sum_of_numbers(a,b):
#     return a + b
# print(sum_of_numbers(5,10))

# Task 2:Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string. Hint: you can use given_character in "aeiou"

# import re
# def vowels(text: str):
#     vowelsMatches = re.findall("[aeiou]", text)
#     return len(vowelsMatches)

# print(vowels(input("Enter sentence:")))

# Task 3:Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise

# def sentence(text: str):
#     letters = list(text)
#     return letters == letters[::-1]
# print(sentence(input("Input word: ")))

# Task 4:Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list

# def integers(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i, end=' ')
# integers([1,3,8,7,11])

# Task 5:Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum.

# - 

# Task 6: Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list.

# def multiply(numbers):
#     result = 1
#     for i in numbers:
#         result = result * i
#     return result
# numbers = [1,2,3,4]
# print(multiply(numbers))

# Task 8:Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value.

# fruits = ("apple", "banana", "cherry", "watermelon", "papaya", "mango", "pineapple", "apricot")
# for fruit in fruits:
#     if fruits.index(fruit) % 2 == 0:
#         print(fruit)

# Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionaries.

# -

# Task 10:Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.

# my_tuple = ("apple", "banana", "cherry")
# my_sec_tuple = []
# for i in my_tuple:
#     my_sec_tuple.append(max(my_tuple))
#     my_sec_tuple.append(min(my_tuple))
#     break
# print(my_sec_tuple)

# Task 11:Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3.

my_set = {3, 18, 2, 1, 11}
my_sec_set = []
for i in my_set:
    if i % 3 != 0:
        my_sec_set.append(i)
print(my_sec_set)












