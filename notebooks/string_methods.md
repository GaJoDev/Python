

## "THIS METHOD WILL OUTPUT EVERYTHING IN LOWER CASE"`.lower()`
## "this method will output everything in upper case"`.upper()`
```Python
print("THIS TEXT WILL BE CONVERTED TO LOWER CASE".lower())
print("this method will output everything in upper case".upper())
print("this method will output everything in title case".title())

#this text will be converted to lower case
#THIS METHOD WILL OUTPUT EVERYTHING IN UPPER CASE
#This Method Will Output Everything In Title Case
```
## Remove surrounding whitespace from a string.

Remove white space from the string with these methods Note - `(repr)` is a debugging method allowing you to view the string representation with hidden characters
```Python
r_strip_result = "            HELLO             ".rstrip()
print(repr(r_strip_result))  # Output: '|HELLO             |'

'            HELLO'

r_strip_result = "            HELLO            ".lstrip()
print(repr(r_strip_result))  # Output: 'HELLO            '

'HELLO            '
```
If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.
```Python
"Forest".endswith("rest") #True

True

"Forest".endswith("trees") #False

False
```
The `isnumeric()` method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error.
```Python
"Forest".isnumeric() #False

False

"12345".isnumeric() #True

True
```
We can also use the join method to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string value of the string object. For example
```Python
" ".join(["This", "example", "concatenates", "each", "word", "in", "the", "sentence", "and", "adds", "the", "contents", "of", "the", 
"first", "string", "in", "between", "each", "letter"])

'This example concatenates each word in the sentence and adds the contents of the first string in between each letter'

"_".join(["This","is","a","sentence"])

'This_is_a_sentence'
```
The inverse of the `.join()` method is the `.split()` method. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.
```Python
string = "This is example splits each word in the sentence".split()
print(string)

['This', 'is', 'example', 'splits', 'each', 'word', 'in', 'the', 'sentence']
```
