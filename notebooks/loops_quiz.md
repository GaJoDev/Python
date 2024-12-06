# loops Quiz

## Question 1

__Fill in the blanks to print the even numbers from 2 to 12.__
```Python
number = ___ # Initialize the variable 
while ___ # Complete the while loop condition
    print(number, end=" ")
    number ___ # Increment the variable

# Should print 2 4 6 8 10 12
```
Solution
```Python
number = 2 # Initialize the variable 
while number <= 12: # Complete the while loop condition
    print(number, end=" ")
    number += 2# Increment the variable

# Should print 2 4 6 8 10 12

2 4 6 8 10 12 
```
## Question 2

__Find and correct the error in the for loop below. The loop should check each number from 1 to 5 and identify if the number is odd or even.__

```Python
for number in range(5,-1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0
```
Solution - needed to include the step element and decrease its value - range(start, stop, step)
```Python
for number in range(5,-1, -1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0
```
## Question 3

__Fill in the blanks to complete the “factorial” function. This function will accept an integer variable “n” through the function parameters and produce the factorials of this number (by multiplying this value by every number less than the original number `[n*(n-1)]`, excluding 0). To do this, the function should:__

- accept an integer variable “n” through the function parameters;

- initialize a variable “result” to the value of the “n” variable;

- iterate over the values of “n” using a while loop until “n” is equal to 0;

- starting at n-1, multiply the result by the current “n” value;

- decrement “n” by -1.

For example, factorial 3 would return the value of 321, which would be 6.
```Python
def factorial(n):
    result = n
    start = n
    n -= 1
    while ___: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        ___ # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1
```
Solution
```Python
def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

6
362880
1
```
## Question 4

__Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication table, where each number is the result of multiplying the first number of its row by the number at the top of its column. Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:__

1 2 3

2 4 6

3 6 9
```Python
def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(___): 
         # Complete the inner loop range
        for y in range(___):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
```
Solution
```Python
def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1, 1):
         # Complete the inner loop range
        for y in range(start, stop+1, 1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()

multiplication_table(1, 3)

1 2 3 
2 4 6 
3 6 9 
```

## Question 5

__Fill in the blanks to complete the “counter” function.__

__This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”.__

__Otherwise, it should count up from “start” to “stop”.__

__Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”__
```Python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            ___ # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            ___ # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
```
Solution
```Python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:   # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:  # Add a comma only if there are more numbers to add
                return_string += ","
            start -= 1  # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop:  # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:  # Add a comma only if there are more numbers to add
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


# Test cases
print(counter(1, 10))  # Should print: "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))   # Should print: "Counting down: 2,1"
print(counter(5, 5))   # Should print: "Counting up: 5"
```
Solution
```Python
for number in range(1, 5+1):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

odd
even
odd
even
odd
```
## Question 3

__Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number. For example, even_numbers(25) should return 13, and even_numbers(6) should return 4. Status: [object Object] 1 point__
```Python
def factorial(n):
    result = n
    start = n
    n -= 1
    while ___: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        ___ # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1
```
Solution
```Python
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            current_number += 2 # Increment the appropriate variable
        count += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

13
73
501
1
```

## Question 4

__Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication table, where each number is the result of multiplying the first number of its row by the number at the top of its column. Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:__

1 2 3

2 4 6

3 6 9
```Python
def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1): 
         # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
# Output:
1 2 3 
2 4 6 
3 6 9 
```
## Question 5

__Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.__
```Python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            ___ # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            ___ # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
```
Solution
```Python
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:   # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start > stop:  # Add a comma only if there are more numbers to add
                return_string += ","
            start -= 1  # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop:  # Complete the while loop
            return_string += str(start) # Add the numbers to the "return_string"
            if start < stop:  # Add a comma only if there are more numbers to add
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


# Test cases
print(counter(1, 10))  # Should print: "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))   # Should print: "Counting down: 2,1"
print(counter(5, 5))   # Should print: "Counting up: 5"

# Output
Counting up: 1,2,3,4,5,6,7,8,9,10
Counting down: 2,1
Counting up: 5
```
## Question 6

__Fill in the blanks to complete the “odd_numbers” function. This function should return a space-separated string of all odd positive numbers, up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “odd_numbers(6)” will return the numbers “1 3 5”.__
```Python
def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for ___: 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        ___  

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed
```
Solution
```Python
def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for i in range (1, maximum+1, 2): 
        print(i, end=" ")
        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.

          

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()

print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

1 3 5 
1 3 5 7 9 
1 
1 3 
```
