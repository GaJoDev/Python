[Python Tutorial: Comprehensions - How they work and why you should be using them](https://www.youtube.com/watch?v=3dt4OGnU5sM)

## Original Task

Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.


```Python
def squares(start, end):
    return [ n*n for n in range(start,end+1 ) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

I wanted to know what was going on to better understand the inner workings of the code, comprehensions are great and all but if you cannot comprehend the result then thats a skill issue!!

The code is using a list comprehension to create a list of squares. This is the solution chatGPT showed me to better undertstand the concept as i could not apply the concept to the problem.

## Solution: Debugging an Unpacked List Comprehension in Python
```Python
def squares(start, end):
    result = []
    for iterator in range(start, end + 1):  # Using 'iterator' as the loop variable
        squared_value = iterator ** 2  # Calculate the square of the current iterator
        print(f"Processing {iterator}: {iterator} squared is {squared_value}")  # Debug output with more detail
        result.append(squared_value)  # Append the squared value to the result

    print(result)  # Print the result after the loop completes
    # return result  # Return the result (commented out as per your request)

# Test the function with different ranges
print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

```
This is the resultant output of the code. The code is using a for loop to iterate over the range of numbers, basically saying to do this until the end of the range (inclusive of itself indicated by `end + 1`) it finds the square of the number indicated by `start` and `end` and prints the square of the number.
```Python
# Iteration 2: 2 squared is 4
# Iteration 3: 3 squared is 9
# [4, 9]
# Iteration 1: 1 squared is 1
# Iteration 2: 2 squared is 4
# Iteration 3: 3 squared is 9
# Iteration 4: 4 squared is 16
# Iteration 5: 5 squared is 25
# [1, 4, 9, 16, 25]
# Iteration 0: 0 squared is 0
# Iteration 1: 1 squared is 1
# Iteration 2: 2 squared is 4
# Iteration 3: 3 squared is 9
# Iteration 4: 4 squared is 16
# Iteration 5: 5 squared is 25
# Iteration 6: 6 squared is 36
# Iteration 7: 7 squared is 49
# Iteration 8: 8 squared is 64
# Iteration 9: 9 squared is 81
# Iteration 10: 10 squared is 100
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## A Relatable Scenario using List Comprehensions

**Task: Organizing a Grocery List**

Imagine you’re managing a grocery store and have a list of items that need to be sorted into categories based on whether they’re perishable or non-perishable. You receive a list of grocery items, each with a name and a type (whether it’s perishable or non-perishable).

**Here’s the list of items:**
```
grocery_items = [
    {"item": "apple", "type": "perishable"},
    {"item": "banana", "type": "perishable"},
    {"item": "rice", "type": "non-perishable"},
    {"item": "canned beans", "type": "non-perishable"},
    {"item": "yogurt", "type": "perishable"},
    {"item": "pasta", "type": "non-perishable"}
]
```
**Task:**

- You want to **separate perishable and non-perishable** items into two separate lists using **list comprehensions**.

### Using List Comprehensions
```Python
# List comprehension to filter perishable items
perishable_items = [item["item"] for item in grocery_items if item["type"] == "perishable"]

# List comprehension to filter non-perishable items
non_perishable_items = [item["item"] for item in grocery_items if item["type"] == "non-perishable"]

# Print the results
print("Perishable Items:", perishable_items)
print("Non-Perishable Items:", non_perishable_items)
```
**Output:**
```Python
Perishable Items: ['apple', 'banana', 'yogurt']
Non-Perishable Items: ['rice', 'canned beans', 'pasta']
```
**What Happened:**

- List comprehension allows you to iterate through `grocery_items` and apply a condition (i.e., check the `"type"` of each item) to filter items into their respective lists.
- In one line, you're able to separate the items based on their type (perishable or non-perishable).

**Real-World Benefit:**

- Instead of using multiple lines with `for` loops and `if` conditions to filter and add items to new lists, the comprehension approach allows you to write clean and concise code.
- If this was part of a larger program (e.g., a grocery store management system), the use of comprehensions makes it much easier to work with data dynamically, such as separating perishable goods for quick sales or inventory updates.

Extended Example: Applying a Transformation

Now, suppose you want to apply a transformation to this data, like capitalizing the names of perishable items to make them stand out in reports. You can do this with a comprehension as well:
```
# List comprehension to capitalize perishable items' names
capitalized_perishables = [item["item"].upper() for item in grocery_items if item["type"] == "perishable"]

# Print the capitalized perishable items
print("Capitalized Perishable Items:", capitalized_perishables)
```
**Output:**
```
Capitalized Perishable Items: ['APPLE', 'BANANA', 'YOGURT']
```
Here, you've filtered the perishable items and transformed them by capitalizing their names, all in one concise comprehension.

**Conclusion:**

In this example, list comprehensions are useful because they let you **filter and transform** data (like sorting grocery items or modifying their appearance) quickly and in a readable way. This not only makes your code more efficient but also more maintainable and easier to understand.