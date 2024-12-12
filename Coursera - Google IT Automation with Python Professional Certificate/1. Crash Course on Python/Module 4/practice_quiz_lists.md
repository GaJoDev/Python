# Your grade: 100%

# Your latest: 100%

# Your highest: 100%

## Question 1

Fill in the blank using a for loop. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code should then generate a new list called "new_filenames" that contains the file names with the new extension.

You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames alone. For this question, you must use a for loop to create the list.

__Problem__
```Python
# Original Question

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = ___
for filename in filenames:
    if filename.endswith("hpp"):
        ___
    else:
        ___


print(new_filenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```
__Solution__
```Python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new = filename.replace("hpp", "h")
        new_filenames.append(new)
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

```


## Question 2

Fill in the blank using a list comprehension. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code function should then generate a new list called "new_filenames" that contains the filenames with the new extension.

You are given a list of filenames like this:

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

Output the list with all of the “.hpp” files renamed to “.h”. Leave the other filenames alone. For this question, you must use list comprehension to create the list.

__Problem__
```Python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
___  # Start your code here

print(new_filenames)
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```
__Solution__

```Python
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

# Start your code here
new_filenames = [filename.replace(".hpp", ".h")for filename in filenames]  

print(new_filenames)
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
```

1 point

## Question 3

Create a function that turns text into pig latin. Pig latin is a simple text transformation that modifies each word by:

- moving the first character to the end of each word;

- then appending the letters "ay" to the end of each word.

For example, python ends up as ythonpay.

__Problem__
```Python
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = ___
  for word in words:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
```
__Solution__
```Python
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
```
1 point

## Question 4

Which list method can be used to add a new element to a list at a specified index position?

[ ] list.pop(index)

__[x] list.insert(index, x)__

[ ] list.add(index, x)

[ ] list.append(x)

1 point

Question 5

Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?

[ ] A tuple is mutable

[ ] A tuple contains only numeric characters

__[x] A tuple is immutable__

[ ] A tuple can contain only one type of data at a time

1 point

Question 6

Fill in the blanks to complete the “biography*list” function. The “biography_list” function reads in a list of tuples “people”, which contains the name, age, and profession of each “person”. Then, prints the sentence "\_\_ is * years old and works as \_\_.". For example, “biography_list([("Ira", 30, "a Chef")])” should print: “Ira is 30 years old and works as a Chef.”

__Problem__
```Python
def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples.
    for ___

        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"
        ___

        # Format the required sentence and place the 3 variables
        # in the correct placeholders using the .format() method.
        print(___.format(___))

# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])

# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer
```
__Solution__
```Python
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
```
