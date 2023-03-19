# 1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 

# import re

# userText = input("Please enter text: \n")
# userLetter = input("Enter letter, which should be found: \n")
# occurrence = userText.count(userLetter)
# if occurrence == 0:
#     print("Entered letter not found")
# else:
#     print("Letter " + str(userLetter) + " is found " + str(occurrence) + " times")

# OR

# text = input("Please enter text: \n")
# letter = input("Enter letter, which should be found: \n")
# occur = re.search(letter, text)
# count = text.count(letter)
# if occur:
#     print("Entered letter matches " + str(count) + " times")
# else:
#     print("Entered letter not found")

# 1.1) Based on the task 1, count the occurrences of each character in the text provided and display them in the output

# userText = input("Please enter text: \n")
# letters = list(userText)
# print(letters)
# for i in letters:
#     occurrences = userText.count(i)
#     print(occurrences, end=" ")

# 2)Write the program to sort the list (without using sort function). You can implement any algorithm

# userText = input("Please enter text: \n").split()
# print(userText)
# text = []
# while userText:
#     minval = min(userText)
#     text.append(minval)
#     userText.remove(minval)
# print(text)
    




