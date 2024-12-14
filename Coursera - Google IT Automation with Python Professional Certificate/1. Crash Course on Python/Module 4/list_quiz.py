'''
Question 1

Fill in the blank using a for loop. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code  should then generate a new list called "new_filenames" that contains the file names with the new extension.

You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames alone. For this question, you must use a for loop to create the list.
'''
# Original Question

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate new_filenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.


# new_filenames = ___
# for filename in filenames:
#     if filename.endswith("hpp"):
#         ___
#     else:
#         ___


# print(new_filenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# # My Solution

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate new_filenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.

# new_filenames = []
# for filename in filenames:
#     if filename.endswith("hpp"):
#         new = filename.replace("hpp", "h")
#         new_filenames.append(new)
#     else:
#         new_filenames.append(filename)


# print(new_filenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# ------------------------------------------

'''
Question 2

Fill in the blank using a list comprehension. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code function should then generate a new list called "new_filenames" that contains the filenames with the new extension.

You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames alone. For this question, you must use list comprehension to create the list.
'''
# Problem
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate new_filenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# ___  # Start your code here


# print(new_filenames)
# # Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# Solution

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [filename.replace(".hpp", ".h")for filename in filenames]  # Start your code here

print(new_filenames)
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# ------------------------------------------

'''
Question 3

Create a function that turns text into pig latin. Pig latin is a simple text transformation that modifies each word by:

  - moving the first character to the end of each word;

  - then appending the letters "ay" to the end of each word.

For example, python ends up as ythonpay.
'''
# PROBLEM

# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = ___
#   for word in words:
#     # Create the pig latin word and add it to the list
#     ___
#     # Turn the list back into a phrase
#   return ___
    
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# SOLUTION

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:] + word[0] + "ay "
  return say
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# Solution commented by chaptGTP

# def pig_latin(text):
#     # Initialize an empty string to store the final Pig Latin sentence.
#     say = ""
    
#     # Split the input text into a list of words. 
#     # The `split()` method breaks the text at each space and returns a list of words.
#     words = text.split()
    
#     # Iterate over each word in the list of words.
#     for word in words:
#         # `word[1:]` takes all characters of the word except the first one (slicing from index 1 onwards).
#         # `word[0]` extracts the first character of the word (at index 0).
#         # Concatenate the modified word in Pig Latin format: the remaining part of the word (`word[1:]`),
#         # the first letter moved to the end (`word[0]`), and the suffix "ay".
#         # Add a space (" ") at the end to separate words in the final sentence.
#         say += word[1:] + word[0] + "ay "
    
#     # Return the full Pig Latin sentence after the loop finishes.
#     # Note: The resulting string will have an extra space at the end, but this is typically harmless.
#     return say

# ------------------------------------------

'''
Fill in the blanks to complete the “biography_list” function. The “biography_list” function reads in a list of tuples “people”, which contains the name, age, and profession of each “person”. Then, prints the sentence "__ is _ years old and works as __.". For example, “biography_list([("Ira", 30, "a Chef")])” should print: “Ira is 30 years old and works as a Chef.”
'''
# PROBLEM

# def biography_list(people):
#     # Iterate over each "person" in the given "people" list of tuples. 
#     for ___ 


#         # Separate the 3 items in each tuple into 3 variables:
#         # "name", "age", and "profession"   
#         ___  


#         # Format the required sentence and place the 3 variables 
#         # in the correct placeholders using the .format() method.
#         print(___.format(___))




# # Call to the function:
# biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# # Click Run to submit code


# # Output should match:
# # Ira is 30 years old and works as a Chef
# # Raj is 35 years old and works as a Lawyer
# # Maria is 25 years old and works as an Engineer

# SOLUTION
def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for person in people:


      # Separate the 3 items in each tuple into 3 variables:
      # "name", "age", and "profession"
      name, age, profession = person
      
    


      # Format the required sentence and place the 3 variables 
      # in the correct placeholders using the .format() method.
      print("{} is {} years old and works as {}".format(name, age, profession))




# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# # Output should match:
# # Ira is 30 years old and works as a Chef
# # Raj is 35 years old and works as a Lawyer
# # Maria is 25 years old and works as an Engineer
# ---------------------------------------

# chatGPT Commented code
# SOLUTION

# def biography_list(people):
#     # Define a function named "biography_list" that takes one parameter: "people".
#     # "people" is expected to be a list of tuples, where each tuple contains 
#     # three elements: a name (string), an age (integer), and a profession (string).

#     # Iterate over each "person" in the given "people" list of tuples.
#     for person in people:
#         # Use a for loop to process each tuple in the "people" list.
#         # Each "person" variable holds one tuple during each iteration of the loop.

#         # Separate the 3 items in each tuple into 3 variables:
#         # "name", "age", and "profession"
#         name, age, profession = person
#         # Unpack the current tuple into three variables: "name", "age", and "profession".
#         # Each element in the tuple is assigned to its corresponding variable by position.

#         # Format the required sentence and place the 3 variables 
#         # in the correct placeholders using the .format() method.
#         print("{} is {} years old and works as {}".format(name, age, profession))
#         # Use the `print` function to output a formatted string.
#         # The `.format()` method is used to insert the values of "name", "age", and "profession"
#         # into their respective placeholders in the string.

# # Call to the function:
# biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])
# # Call the "biography_list" function with a list of tuples as its argument.
# # Each tuple contains a name, an age, and a profession.

# # # Output should match:
# # # Ira is 30 years old and works as a Chef
# # # Raj is 35 years old and works as a Lawyer
# # # Maria is 25 years old and works as an Engineer

