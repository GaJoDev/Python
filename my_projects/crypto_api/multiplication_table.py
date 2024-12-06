def check_input():
    while True:
        # Prompt the user to enter a number
        user_input = input("Please enter a number: ")
        if user_input.isdigit():
            # Convert the valid integer string to an integer
            str_to_int = int(user_input)
        
            # Check if the integer is within the valid range (1 to 12, inclusive)
            if str_to_int >= 1 and str_to_int <= 12:
                # Inform the user that the input is valid and display the number
                # print("yay!, it's a valid request!, here is the valid number: ", str_to_int)
                # Optionally, you could use 'return' here to exit the function
                return str_to_int
            else:
                # Inform the user that the number is out of range and prompt again
                print("Please enter a number between 1 and 12")

        else:
            # Inform the user that the input is not a valid integer and prompt again
            print("The input is not an integer. Try again")


# this is the return value from check_input() being assigned to an integer
multiplier = check_input()

def multiplication_function(multiplier):
    # print(multiplier, "is the return value from the check_input() function")
    # print("str_to_int type", (type(multiplier)))
    
    for i in range(1): 
        # Print a message that includes the current loop number
        # "i" represents the current number in the loop (1, 2, 3, ..., 10)
        print("Here is the multiplication table for the multiplier :", multiplier)
        for j in range(1, 12+1):
            # Print a message that includes the current loop number
            # "j" represents the current number in the loop (1, 2, 3
            # ..., 10)
            print(f"{j} x {multiplier} =", j*multiplier)



## Now need to work out how to loop through the numbers 1 to 12 and multiply each number by the user inputted number
## and then print out the results in a table format.


multiplication_function(multiplier)