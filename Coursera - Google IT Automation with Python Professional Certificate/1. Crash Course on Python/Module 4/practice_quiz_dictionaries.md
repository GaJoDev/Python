**Your grade: 80**

**Your latest: 80**

**Your highest: 80**

## Question 1

The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

__Problem__
```Python
def email_list(domains):
    emails = []
    for ___:
      for user in users:
        emails.___
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
```
__Solution__
```Python
def email_list(domains):
    # Step 1: Initialize an empty list named `emails` to store the resulting email addresses.
    # This list will be populated as we process the `domains` dictionary.
    emails = []
    
    # Step 2: Begin iterating over the dictionary `domains` using the `.items()` method.
    # `.items()` returns each key-value pair as a tuple where:
    #   - `domain` is the key (e.g., "gmail.com", "yahoo.com").
    #   - `users` is the value (a list of usernames associated with the domain).
    for domain, users in domains.items():
        # Step 3: For each domain, iterate through the list of usernames (`users`) associated with it.
        for user in users:
            # Step 4: Construct an email address by concatenating:
            #   - The `user` (username) string.
            #   - The "@" character.
            #   - The `domain` string.
            # The `+` operator combines these strings into the format: username@domain.
            email_address = user + "@" + domain
            
            # Step 5: Append the constructed email address to the `emails` list.
            emails.append(email_address)
    
    # Step 6: Once all usernames and domains have been processed, return the populated `emails` list.
    return emails

# Step 7: Call the `email_list` function with a dictionary as input.
# The dictionary contains email domains as keys and lists of usernames as values.
# For example:
#   - "gmail.com" has three usernames: ["clark.kent", "diana.prince", "peter.parker"]
#   - "yahoo.com" has two usernames: ["barbara.gordon", "jean.grey"]
#   - "hotmail.com" has one username: ["bruce.wayne"]
# The function generates a list of email addresses for these users and returns it.
result = email_list({
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],  # Domain 1: Three users
    "yahoo.com": ["barbara.gordon", "jean.grey"],                 # Domain 2: Two users
    "hotmail.com": ["bruce.wayne"]                               # Domain 3: One user
})

# Step 8: Print the resulting list of email addresses.
print(result)

# Expected output:
# [
#   "clark.kent@gmail.com",
#   "diana.prince@gmail.com",
#   "peter.parker@gmail.com",
#   "barbara.gordon@yahoo.com",
#   "jean.grey@yahoo.com",
#   "bruce.wayne@hotmail.com"
# ]

```
1 point

## Question 2

The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

```Python
def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group_name, groups in group_dictionary.items():
        # Now add the group to the the list of
        # # groups for this user, creating the entry
        # # in the dictionary if necessary
        
        # Now go through the users in the group
        for user in groups:
        # Now add the group to the the list of
        # # groups for this user, creating the entry
        # # in the dictionary if necessary
                if user in user_groups:
                     user_groups[user].append(group_name)
                else:
                     user_groups[user] = [group_name]

    return(user_groups)

print(groups_per_user(
    {
        "local":["admin", "userA"],
        "public":["admin", "userB"],
        "administrator":["admin"]
    }))
```
1 point

## Question 3

The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?
```
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
```


[ ] `{'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}`

[ ] `{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}`

[x] `{'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black', 'white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}`

[] `{'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}`

1 point

## Question 4

What’s a major advantage of using dictionaries over lists?

[ ] *Dictionaries are ordered sets*

[ ] *Dictionaries can be accessed by the index number of the element*

[ ] *Elements can be removed and inserted into dictionaries*

[x] **It’s quicker and easier to find a specific element in a dictionary**
5.

1 point

## Question 5

The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

Problem
```Python
def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for ___:
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += ___
    # Limit the return value to 2 decimal places
    return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
```
Solution
```Python
def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for basket,  item in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += item
    # Limit the return value to 2 decimal places
    return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
```


1 point