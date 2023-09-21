# Python - Everything is object

## What is an object:
    In Python, an object is a fundamental concept. Everything in Python is an object, including integers, strings, lists, functions, and even classes. An object is a self-contained unit that contains both data (attributes) and behavior (methods).

## What is the difference between a class and an object or instance:
        A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that objects of that class will have.
        An object, also known as an instance, is a concrete instantiation of a class. It represents a specific item or entity created based on the class's blueprint.

## What is the difference between an immutable object and a mutable object:
        Immutable objects are objects whose state (the data they hold) cannot be modified after creation. Examples include integers, strings, and tuples.
        Mutable objects, on the other hand, can be modified after creation. Examples include lists, dictionaries, and sets.

## What is a reference:
    A reference in Python is essentially a pointer or a link to an object's memory location. When you create a variable and assign it a value, you are creating a reference to the object containing that value.

## What is an assignment:
    Assignment is the process of giving a value (object) to a variable. It associates a name with a reference to an object in memory.

## What is an alias:
    An alias is when two or more variables reference the same object. Changes made to one variable may affect the object, and these changes will be visible through other variables that reference the same object.

## How to know if two variables are identical:
    You can use the is operator to check if two variables reference the same object. For example: x is y.

## How to know if two variables are linked to the same object:
    You can use the is operator to check if two variables reference the same object, as mentioned in the previous answer.

## How to display the variable identifier (which is the memory address in the CPython implementation):
    You can use the id() function to get the memory address (identifier) of an object. For example: print(id(x)).

## What is mutable and immutable:
    Mutable objects can be changed after creation, while immutable objects cannot be changed after creation.

## What are the built-in mutable types:
    Some built-in mutable types in Python include lists, dictionaries, and sets.

## What are the built-in immutable types:
    Some built-in immutable types in Python include integers, floats, strings, tuples, and frozensets.

## How does Python pass variables to functions:
    Python passes variables to functions by passing references to objects. When you pass a variable to a function, you are passing a reference to the object that the variable points to. This means that changes made to the object within the function can affect the object outside the function if it's mutable. Immutable objects cannot be changed, so they behave as if they were copied when passed to a function.
