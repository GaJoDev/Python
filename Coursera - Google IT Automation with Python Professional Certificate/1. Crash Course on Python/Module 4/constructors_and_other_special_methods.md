
# Constructors and Other Special Methods (Optional)

As you have been learning, you can use a class in Python to bundle data and functionality together. When you create a new class, you create a new type of object.

Creating an instance of a class

Each time you create an instance of a class, Python calls a special class method the constructor. The constructor’s job is to set up the object, meaning that instance of the class, so it’s ready to be used. Usually this means initializing some variables and doing other simple housekeeping.

When writing a Python class, you define a method called __init__ to be your constructor. The special name tells Python to use that method as the constructor. Just like any other method, the constructor can take arguments. When making an argument to the class, the first constructor must always be self.

Here’s a simple example of a constructor that initializes an object’s variables.

```Python
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.color)
# prints "red"
```
Modify variables

If we wanted to make our Apple class more flexible, we could allow the user to specify the color and flavor as arguments when creating the object. We can modify our constructor to take those arguments and use them:
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)
# prints "sweet" and "tart"

```
Other special methods

As you might expect, Python classes have many other special methods. Most of these have default implementations provided by the Python standard library, but you are free to override the behavior of any of them. Like the `__init__` constructor, special methods begin and end with a double underscore, and this is called dunder method. The word “dunder” combines the “d” in double and the “under” in underscore.

For example, the `__str__` special method controls how your object is converted to a string representation for output. When you print() something, Python calls the object’s `__str__`() method and outputs whatever that method returns. In most cases, the default output is just the class name and a memory location:

```Python
>>> print(honeycrisp) <__main__.Apple object at 0x7ffa68d78970>
```
Let’s override the __str__ method to be more useful for apples:
```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
honeycrisp = Apple("red", "sweet")
print(honeycrisp)
# prints "an apple which is red and sweet"
```
Here are some of the other special methods you can override in your own classes:

-   `__len__` returns the length of the object or collection.
    
-   `__contains__` tests whether the object contains an item.
    
-   `__eq__` tests whether two objects are equal.
    

Key takeaways

A constructor (such as `__init__`) is a special class method that sets up the object in Python. When making an argument to a class, the first constructor must always be `self`. Python classes have many special methods available in the standard library. These methods can be overridden using the method called dunder method.

# Special Methods

Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a **constructor**. Below is an example of an Apple class with a constructor method defined.

```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
```
When you call the name of a class, the constructor of that class is called. This constructor method is always named **__init__**. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:

```Python
jonagold = Apple("red", "sweet")
print(jonagold.color)
```

In addition to the **__init__** constructor special method, there is also the **__str__** special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the **__str__** method added:

```Python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

```

Now, when we pass an Apple object to the print function, we get a nice formatted string:

```Python
jonagold = Apple("red", "sweet")
print(jonagold)
```
This apple is red and its flavor is sweet

It's good practice to think about how your class might be used and to define a __str__ method when creating objects that you may want to print later.

# Methods as special operators

You have already learned about methods and how they are just functions that belong to a class. They define the behavior that an object of the class can perform. Special operators are specific symbols or keywords that are built-in and provide special behavior when used with certain data types or objects. In your class, you can define methods to implement or override the standard behavior of Python operators, thus creating methods as special operators.

In this reading you will learn about the different types of special operators, how to override the standard operators and embed them in your code, and see examples along the way.

## **Different types of special operators**

Python supports a variety of different operators that you can use in your code to make life easier for you. Some of the more common operators are:

-   Arithmetic operators. These include `+` (addition), `-` (subtraction), `*` (multiplication), / (division), and `**` (exponentiation).
    
-   Comparison operators. These include `==` (equality), `!=` (inequality), < (less than), and `>=` (greater than or equal to)
    
-   Logical operators. These include `and`, `or`, and `not`.
    
-   Assignment operators. These include = (simple assignment), += (addition assignment), and %= (modulo assignment)
    

**Note:** This is not an all-inclusive list, but different examples of common operators that you would use in Python.

## **Performing special operations**

Every special operator has a corresponding **dunder method** that implements the operation. In Python, you denote a dunder method by placing double underscores at the beginning and end of the name; in fact, the term “dunder” comes from this use of **d**ouble **unders**cores. You can change how an operator behaves with an instance of your object by overriding the implementation. Let’s look at an example:
```Python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
```
In this example, the Triangle class has a method __init__()which is called a constructor and is used to initialize the object’s attributes.

```Python
def area(self):
return 0.5 * self.base * self.height
```
This part of the code, area(self) method, computes the area of the triangle based on its height and base length.
```Python
def __add__(self, other):
return self.area() + other.area()
```
This method overrides the + operator to "add" two triangles together.
```Python
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
```
The output of this problem is:
```Python
The area of triangle 1 is 25.0
The area of triangle 2 is 24.0
The area of both triangles is 49.0
```
Putting it all together, this is what the code should look like:
```Python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()
    
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
```
For a full list of operators and the method names you can use to override their behavior, view this resource:

-   [Mapping operators to functions](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)
    

## **Key takeaways**

Python allows you to override or implement standard operations in your code to make your code cleaner for yourself and others to read. Being able to override certain behaviors allows you to control the output of your code and provides flexibility in how you write code.