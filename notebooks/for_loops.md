# for Loops

## Print Numbers 1 to 10

Write a program that prints the numbers from 1 to 10, one per line.
```Python
# Start a loop that will iterate over a range of numbers
# range(1, 11) generates numbers from 1 to 10 (11 is not included)
for i in range(1, 10+1):  
    # Print a message that includes the current loop number
    # "i" represents the current number in the loop (1, 2, 3, ..., 10)
    print("current value of i: ", i)

current value of i:  1
current value of i:  2
current value of i:  3
current value of i:  4
current value of i:  5
current value of i:  6
current value of i:  7
current value of i:  8
current value of i:  9
current value of i:  10
```
Explanation of the Comments:

Loop Through Numbers: The range(1, 11) function generates a sequence of numbers from 1 to 10. This is used to control how many times the loop will run. The first argument (1) is the starting value, and the second argument (11) is the endpoint, but it's exclusive, so the loop stops at 10.

Iteration Output: Inside the loop, the print("Iteration: ", i) statement will display the current iteration number. The variable i holds the value of the current number from the range, starting at 1 and ending at 10. Each time the loop runs, it prints the message "Iteration: " followed by the current value of i.

This structure allows you to track how many times the loop has executed and which value it is processing at each iteration.

Write a program that calculates the sum of all numbers from 1 to n (inclusive). For example, if n = 5, the sum should be 1 + 2 + 3 + 4 + 5 = 15.
```Python
# Define the value of n, which is the upper limit of the range
n = 5

# Initialize the sum variable to 0
sum = 0

# Iterate over the range of numbers from 1 to n (inclusive)
for i in range(1, n + 1):
    # Add the current value of i to the sum
    sum += i
    
    # Check if the current number is not the last number (n)
    if i != n:
        # If it's not the last number, print the number followed by a "+", staying on the same line
        print(i, "+ ", end="")
    else:
        # If it's the last number, print the number without the "+", followed by a newline
        print(i, end=" ")
        
# After the loop, print the sum of all numbers from 1 to n
print("=", sum)

1 + 2 + 3 + 4 + 5 = 15
```
Count Even Numbers

Write a program that counts how many even numbers there are between 1 and n. For example, for n = 10, the even numbers are 2, 4, 6, 8, and 10, so the count should be 5.
```Python
n = 10
even_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
print("Even numbers count:", even_count)

Even numbers count: 5

Find Divisible Numbers

Write a program that finds all numbers between 0 and n that are divisible by a given number divisor. For example, if n = 20 and divisor = 3, it should print numbers like 0, 3, 6, 9, 12, 15, 18.
```Python
n = 20
divisor = 3
for i in range(0, n + 1):
    if i % divisor == 0:
        print(i)
```
0
3
6
9
12
15
18

Count Even Numbers

Write a program that counts how many even numbers there are between 1 and n. For example, for n = 10, the even numbers are 2, 4, 6, 8, and 10, so the count should be 5.
```Python
n = 10
even_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
print("Even numbers count:", even_count)

Even numbers count: 5
```
Multiplication Table

Write a program that prints the multiplication table for a given number. For example, for the number 5, it should print:

5 x 1 = 5 5 x 2 = 10 5 x 3 = 15 ... 5 x 10 = 50
```Python
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
Print Squares of Numbers

Write a program that prints the squares of numbers from 1 to n. For example, for n = 5, it should print:

1 4 9 16 25
```Python
n = 5
for i in range(1, n + 1):
    print(i ** 2)
```
1
4
9
16
25



## Countdown from n

Write a program that counts down from a number n to 1, printing each number on a new line.

```Python
def countdown(n):
    for i in range(n, 0, -1):  # Start from n, stop before 0, decrement by 1
        print(i)

# Example usage:
countdown(5)

# Ouput
5
4
3
2
1
```

## Print Odd Numbers

__Write a program that prints all odd numbers between 1 and n. For example, for n = 10, it should print: 1, 3, 5, 7, 9.__

```Python
n = 10 for i in range(1, n + 1, 2): # Increment by 2 to get odd numbers print(i)

n = 10
for i in range(1, n + 1, 2):  # Increment by 2 to get odd numbers
    print(i)
```
## Factorial of a Number

__Write a program that calculates the factorial of a number n. The factorial of a number is the product of all positive integers less than or equal to n. For example, 5! = 5 4 3 2 1 = 120.__
```Python
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)
```
## Print Numbers Divisible by 3 or 5

__Write a program that prints all numbers between 1 and n that are divisible by either 3 or 5. For example, for n = 15, the numbers should be: 3, 5, 6, 9, 10, 12.__
```Python
n = 15
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

3
5
6
9
10
12
15
```
