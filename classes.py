


# Introduction to Classes in Python

## What is a Class?

A class in Python is a blueprint for creating objects. Objects are instances of classes that encapsulate data (attributes) and behaviors (methods) related to a specific entity or concept.

### Key Concepts:

1. **Class**: A template for creating objects.
2. **Object**: An instance of a class.
3. **Attributes**: Variables that hold data specific to an object.
4. **Methods**: Functions defined within a class that describe the behaviors of an object.

---

## Defining a Class

In Python, a class is defined using the `class` keyword:

```python
class ClassName:
    # Class body
    pass
```

### Example:

```python
class Vehicle:
    pass
```

This defines a simple `Vehicle` class with no attributes or methods yet.

---

## Creating Objects (Instances)

To create an object from a class, you call the class as if it were a function:

```python
car1 = Vehicle()
```

Here, `car1` is an instance of the `Vehicle` class.

---

## Adding an Initialization Method (`__init__`)

The `__init__` method is a special method in Python that initializes an object’s attributes when the object is created.

### Syntax:

```python
class ClassName:
    def __init__(self, arg1, arg2):
        self.attribute1 = arg1
        self.attribute2 = arg2
```

### Example:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating an object with attributes
car1 = Vehicle("Toyota", "Corolla")
print(car1.make)  # Output: Toyota
print(car1.model) # Output: Corolla
```

---

## Adding Methods

Methods are functions defined inside a class that operate on an object’s attributes or perform specific actions.

### Example:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} starts moving!")

# Creating an object and calling a method
car1 = Vehicle("Toyota", "Corolla")
car1.start()  # Output: The Toyota Corolla starts moving!
```

---

## Understanding `self`

- The `self` parameter is a reference to the current instance of the class.
- It must be the first parameter of any method in the class.
- Through `self`, you can access an object’s attributes and other methods.

### Example:

```python
class Vehicle:
    def __init__(self, make):
        self.make = make

    def describe(self):
        print(f"This vehicle is a {self.make}.")
```

---

## Class vs. Instance Attributes

### Instance Attributes:

- Defined within the `__init__` method.
- Unique to each instance.

### Class Attributes:

- Shared across all instances of the class.
- Defined outside any method, directly within the class body.

### Example:

```python
class Vehicle:
    category = "Automobile"  # Class attribute

    def __init__(self, make):
        self.make = make  # Instance attribute

# Accessing class and instance attributes
car1 = Vehicle("Toyota")
print(car1.category)  # Output: Automobile
print(car1.make)     # Output: Toyota
```

---

## Class Variables

Class variables are variables that are shared across all instances of a class. Unlike instance variables, which are unique to each instance, class variables hold the same value for every object unless explicitly changed.

### Example:

```python
class Library:
    total_books = 1000  # Class variable

    def __init__(self, branch_name):
        self.branch_name = branch_name  # Instance variable

    def borrow_book(self):
        if Library.total_books > 0:
            Library.total_books -= 1
            print(f"A book was borrowed from {self.branch_name}. Remaining books: {Library.total_books}")
        else:
            print("No books available.")

# Accessing class variables
main_branch = Library("Main Branch")
sub_branch = Library("Sub Branch")

main_branch.borrow_book()  # Output: A book was borrowed from Main Branch. Remaining books: 999
sub_branch.borrow_book()   # Output: A book was borrowed from Sub Branch. Remaining books: 998
```

### Key Points:

- Class variables are defined at the class level.
- They can be accessed and modified using the class name (e.g., `Library.total_books`).
- Changes to a class variable affect all instances of the class.

---

## Class Methods and Static Methods

### Class Methods

Class methods are methods that operate on the class itself rather than individual instances. They are defined using the `@classmethod` decorator and take `cls` (the class itself) as the first parameter.

### Example:

```python
class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

# Creating objects and accessing class methods
car1 = Vehicle("Toyota", "Corolla")
car2 = Vehicle("Honda", "Civic")
print(Vehicle.get_vehicle_count())  # Output: 2
```

### Key Points:

- Class methods are used when you need to access or modify class-level attributes.
- They work on the class level, not specific instances.

---

### Static Methods

Static methods are utility methods that do not depend on class-level or instance-level data. They are defined using the `@staticmethod` decorator and do not take `self` or `cls` as a parameter.

### Example:

```python
class Vehicle:
    @staticmethod
    def is_motorized(vehicle_type):
        motorized_types = ["car", "truck", "motorcycle"]
        return vehicle_type in motorized_types

# Using static methods
print(Vehicle.is_motorized("car"))       # Output: True
print(Vehicle.is_motorized("bicycle"))  # Output: False
```

### Key Points:

- Static methods are used for functionality related to the class but independent of any specific object or the class itself.
- They act like regular functions but are part of the class's namespace.

---

## Inheritance

Inheritance allows a class (child class) to derive attributes and methods from another class (parent class).

### Example:

```python
class Machine:
    def __init__(self, name):
        self.name = name

    def operate(self):
        print("This machine is operating.")

class Vehicle(Machine):
    def operate(self):
        print(f"The {self.name} is driving.")

# Creating an object from the child class
car1 = Vehicle("Toyota Corolla")
car1.operate()  # Output: The Toyota Corolla is driving.
```
## Encapsulation and Access Control

Encapsulation restricts direct access to some of an object’s components to enforce controlled interaction.

### Example:

```python
class Vehicle:
    def __init__(self, make):
        self.__make = make  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

# Accessing private attributes via methods
car1 = Vehicle("Toyota")
print(car1.get_make())  # Output: Toyota
car1.set_make("Honda")
print(car1.get_make())  # Output: Honda
```
---

**Summary**

Classes are blueprints for objects.

Objects are instances of classes with unique data.

The __init__ method initializes attributes.

Use `self` to refer to the current instance.

Class attributes are shared, while instance attributes are unique.

Class variables hold shared data for all instances.

Class methods operate on the class itself.

Static methods provide utility functions independent of instances or class-level data.

Inheritance allows reusing and extending functionality.

Use encapsulation for controlled data access.

## Creating Subclasses in Python

In Python, subclasses are used to create a new class that is derived from an existing class (the base class). Subclasses inherit the attributes and methods of the parent class, but they can also have additional attributes and methods or override the parent class methods.

Let's explore this concept using a `Vehicle` class and a subclass called `Car`.

#### Step 1: Defining the Parent Class (Vehicle)
We begin by defining a `Vehicle` class, which will serve as the base class for all types of vehicles.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")

#### Step 2: Creating a Subclass (Car)
Next, we create a subclass called `Car`, which inherits from `Vehicle`. The `Car` class can access all the attributes and methods of `Vehicle`, but we can also add unique features or override existing methods.
```Python
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        # Call the parent class's __init__ method to initialize common attributes
        super().__init__(make, model, year)
        self.doors = doors  # Additional attribute for the Car class

    def start(self):
        # Override the start method for the Car subclass
        print(f"The {self.year} {self.make} {self.model} with {self.doors} doors is starting.")
```
#### Step 3: Instantiating Objects from Subclasses
Once the subclass is defined, we can create instances of both the `Vehicle` and `Car` classes.
```Python
## Creating an instance of the Vehicle class
vehicle = Vehicle("Toyota", "Corolla", 2020)
vehicle.start()  # Outputs: The 2020 Toyota Corolla is starting.
vehicle.stop()   # Outputs: The 2020 Toyota Corolla is stopping.

# Creating an instance of the Car class
car = Car("Honda", "Civic", 2022, 4)
car.start()      # Outputs: The 2022 Honda Civic with 4 doors is starting.
car.stop()       # Outputs: The 2022 Honda Civic is stopping.
```
#### Key Points About Subclasses:
- **Inheritance**: Subclasses inherit the attributes and methods of the parent class, but they can also define their own.
- **Method Overriding**: Subclasses can override methods from the parent class to provide a more specific implementation.
- **Calling Parent Methods**: The `super()` function allows us to call the methods of the parent class, enabling us to build on existing functionality.


### Special (Magic/Dunder) Methods in Python

Special methods, also known as magic or dunder (double underscore) methods, are predefined methods in Python that allow you to define custom behavior for built-in operations. These methods are surrounded by double underscores (e.g., `__init__`, `__str__`, `__add__`) and are called implicitly when specific operations are performed.

#### Enhancing the `Car` Class with Special Methods

Let's explore some commonly used special methods by enhancing the `Car` class.

#### `__str__` Method
The `__str__` method defines how an object is represented as a string, such as when using `print()`.

```python
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def start(self):
        print(f"The {self.year} {self.make} {self.model} with {self.doors} doors is starting.")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.doors} doors)"
```

Now, if we print a `Car` object, it provides a more descriptive output.

```python
car = Car("Honda", "Civic", 2022, 4)
print(car)  # Outputs: 2022 Honda Civic (4 doors)
```

#### `__eq__` Method
The `__eq__` method is used to define custom equality checks between two objects. For example, two `Car` objects can be considered equal if they have the same make, model, year, and doors.

```python
    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return (self.make == other.make and 
                self.model == other.model and 
                self.year == other.year and 
                self.doors == other.doors)
```

Example usage:

```python
car1 = Car("Honda", "Civic", 2022, 4)
car2 = Car("Honda", "Civic", 2022, 4)
car3 = Car("Toyota", "Corolla", 2021, 4)

print(car1 == car2)  # Outputs: True
print(car1 == car3)  # Outputs: False
```

#### `__repr__` Method
The `__repr__` method is intended to provide a developer-friendly representation of the object, often useful for debugging.

```python
    def __repr__(self):
        return f"Car(make={self.make!r}, model={self.model!r}, year={self.year!r}, doors={self.doors!r})"
```

Example usage:

```python
print(repr(car))  # Outputs: Car(make='Honda', model='Civic', year=2022, doors=4)
```

#### Summary of Common Special Methods
- `__init__`: Initializes the object when it's created.
- `__str__`: Returns a readable string representation of the object.
- `__repr__`: Returns an unambiguous string representation of the object, useful for debugging.
- `__eq__`: Defines how equality is determined for the object.
- `__len__`, `__getitem__`, `__add__`, and others: Provide custom behavior for built-in operations like `len()`, indexing, and addition.

By using these special methods, we can make classes more intuitive and user-friendly while tailoring them to specific requirements.


### Property Decorators: Getters, Setters, and Deleters

In Python, property decorators provide a Pythonic way to define getters, setters, and deleters for class attributes. They enable controlled access to private or protected attributes, ensuring encapsulation and validation when needed.

#### Adding Properties to the `Car` Class

Let's enhance the `Car` class by adding properties for an attribute called `price`.

#### `@property` Decorator
The `@property` decorator is used to define a getter method for an attribute. It allows you to access the attribute like a regular property while keeping the internal implementation hidden.

```python
class Car(Vehicle):
    def __init__(self, make, model, year, doors, price):
        super().__init__(make, model, year)
        self.doors = doors
        self._price = price  # Use a protected attribute

    @property
    def price(self):
        return self._price
```

Example usage:

```python
car = Car("Honda", "Civic", 2022, 4, 25000)
print(car.price)  # Outputs: 25000
```

#### `@price.setter` Decorator
The `@price.setter` decorator allows you to define a method to set the value of an attribute. This is useful for adding validation or logging changes.

```python
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value
```

Example usage:

```python
car.price = 26000
print(car.price)  # Outputs: 26000

# Attempting to set a negative price
car.price = -5000  # Raises ValueError: Price cannot be negative.
```

#### `@price.deleter` Decorator
The `@price.deleter` decorator allows you to define a method to delete an attribute. This might be useful for cleanup or when removing sensitive data.

```python
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
```

Example usage:

```python
del car.price  # Outputs: Deleting price...
```

#### Summary of Property Decorators
- `@property`: Defines a getter method for an attribute.
- `@attribute.setter`: Defines a setter method to modify an attribute's value, with optional validation.
- `@attribute.deleter`: Defines a deleter method to remove an attribute.

Using property decorators, we can control access to class attributes, ensuring better encapsulation and data integrity while maintaining a clean and intuitive API.

