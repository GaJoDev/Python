## Python Dictionaries

## Accessing and Writing Data

Values in a Python dictionary can be accessed by placing the key within square brackets next to the dictionary. Values can be written by placing key within square brackets next to the dictionary and using the assignment operator `=`. If the key already exists, the old value will be overwritten. Attempting to access a value with a key that does not exist will cause a KeyError.

To illustrate this review card, the second line of the example code block shows the way to access the value using the key `["song"]`. The third line of the code block overwrites the value that corresponds to the key `["song"]`.
```Python
my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
```

## Syntax

The syntax for a Python dictionary begins with the left curly brace `{` ends with the right curly brace `}` and contains zero or more `"key"` `:` `"value"` items separated by commas `,`. The `"key"` is separated from the `"value"` by a colon `:`.

**Note:** This guide will use double quotes and single quo
```Python
roaster = {"q1": "Ashley", "q2": "Dolly"}
```

## Merging Dictionaries With The `.update()` Method

Given two dictionaries that need to be combined, Python makes this easy with the `.update()` function.

For `dict1.update(dict2)`, the key-value pairs of `dict2` will be written into the `dict1` dictionary.

For keys in both `dict1` and `dict2`, the value in `dict1` will be overwritten by the corresponding value in `dict2`.
```Python
dict1 = {"color": "blue", "shape": "circle"}
dict2 = {"color": "red", "number": 42}

dict1.update(dict2)

# dict1 is now {"color": "red", "shape": "circle", "number": 42}
```

## Dictionary Value Types

Python allows the `"values"` in a dictionary to be any type – string, integer, a list, another dictionary, boolean, etc. However, `"keys"` must always be an immutable data type, such as **strings**, **numbers**, or **tuples**.

In the example code block, you can see that the keys are strings or numbers (**int** or **float**). The values, on the other hand, are many varied data types.
```Python
dictionary = {
  1: "hello", 
  "two": True, 
  "3": [1, 2, 3], 
  "Four": {"fun": "addition"}, 
  5.0: 5.5
}
```

## Python Dictionaries

A python dictionary is an unordered collection of items. It contains data as a set of `"key"`:`"value"` pairs.
```Python
my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets"}
```

## Key-Value Methods

When trying to look at the information in a Python dictionary, there are multiple methods that return objects that contain the dictionary keys and values.

- `.keys()` returns the keys through a `dict_keys` object.
- `.values()` returns the values through a `dict_values` object.
- `.items()` returns both the keys and values through a `dict_items` object.

```Python
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex_dict.keys()
# dict_keys(["a","b","c"])

ex_dict.values()
# dict_values(["anteater", "bumblebee", "cheetah"])

ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])
```

## .get() Method

Python provides a `.get()` method to access a `dictionary` value if it exists. This method takes the `key` as the first argument and an optional default value as the second argument, and it returns the value for the specified key if key is in the dictionary. If the second argument is not specified and `key` is not found then `None` is returned.
```Python
# without default
{"name": "Victor"}.get("name")
# returns "Victor"

{"name": "Victor"}.get("nickname")
# returns None

# with default
{"name": "Victor"}.get("nickname", "nickname is not a key")
# returns "nickname is not a key"
```

## .pop() Method

 Dictionaries can remove key-value pairs with the .pop() method. The method takes a key as an argument and removes it from the dictionary. At the same time, it also returns the value that it removes from the dictionary.
```Python
famous_museums = {"Washington": "Smithsonian Institution", "Paris": "Le Louvre", "Athens": "The Acropolis Museum"}
removed_value = famous_museums.pop("Athens")
print(removed_value)  # Output: The Acropolis Museum
print(famous_museums) # {"Washington": "Smithsonian Institution", "Paris": "Le Louvre"}
```
### Practical Use of .pop()

This behavior is useful when you need to:

- Remove and keep track of a specific item:
    ```Python
    last_museum = famous_museums.pop("Athens")
    print(last_museum)  # Output: The Acropolis Museum
    ```
- Avoid Key Errors: You can provide a default value as the second argument to .pop() in case the key doesn’t exist:
    ```Python
    result = famous_museums.pop("London", "Key not found")
    print(result)  # Output: Key not found
    ```

## Best Practices for Using Quote Types in Python Dictionaries

1. Choose a Consistent Style:
    - Consistency in your codebase is more important than whether you use single or double quotes.
    - Pick one and stick to it within a project or file. This makes your code easier to read and avoids confusion.

2. Double Quotes are Often Preferred in Python:
    - While Python allows both, many developers and popular style guides (e.g., [PEP 8](https://peps.python.org/pep-0008/)) prefer double quotes (") for strings. This is because:
    - Double quotes are consistent with JSON, which uses double quotes exclusively.
    - They are common in other programming languages, making the code more familiar to developers.

3. When to Use Single Quotes (`'`):

    - Use single quotes when the string contains double quotes, to avoid the need for escaping:
    ```Python
    dialogue = {'quote': 'He said, "Hello!"'}
    ```
    - Similarly, use double quotes if the string contains single quotes:
    ```Python
    example = {"phrase": "It's sunny today"}
    ```

4. 
    - Avoid mixing single and double quotes arbitrarily within the same dictionary or file. It can be confusing:

    ```Python
    # Consistent
    my_dict = {"color": "red", "shape": "circle"}
    ```
    or
    ```Python
    my_dict = {'color': 'red', 'shape': 'circle'}
    ```

    ### Summary

    - Consistency is the most important factor.
    - Prefer double quotes `"` for compatibility with JSON and broader conventions, your project or style guide says otherwise.
    - Use the type of quotes that avoids unnecessary escaping if the string contains quotes.