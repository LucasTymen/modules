"""
https://www.codecademy.com/resources/docs/python/random-module

    Docs/
    Python/
    Random Module

Random Module

In Python, the built-in random module is used to randomly generate numbers as well as randomly manipulate collections such as lists and strings.

This module can be used when imported at the top of a Python file:
"""
import random
"""
The random variable can then be used for executing the module’s built-in methods, like the .random() method below:
"""
random.random()
"""
Random Module

###########################  .choice()  ###########################
    Returns a random item chosen from an iterable argument, such as a list or a dictionary.
The .choice() method returns a random item chosen from an iterable argument, such as a list or a dictionary.
Syntax

random.choice(iterable)

An iterable can be any kind of sequence-oriented variable, including:

    A string of characters ("Hello, World!").
    A range of steps (range(10)).
    A list of items ([0, 1]).
    A tuple of data values ((0, "one")).

exemple:
"""
import random

to_learn = ("Python",
            "Matplotlib",
            "NumPy",
            "Pandas",
            "Beautiful Soup",
            "SQL")

print(random.choice(to_learn))
"""

###########################  .randint()  ###########################
    Returns a random integer that exists between two values.
The .randint() method returns a random integer that exists between two int values, int_a and int_b (inclusive), passed as arguments.
Syntax

random.randint(int_a, int_b)

Another way of writing this would be random.randrange(int_a, int_b + 1).

Example:

In the example below, .randint() is used to return a random number between 0 and 50:
"""
import random

print(random.randint(0, 50))
"""
Codebtye Example

The .randint() method can also be applied to negative int values, as shown in the example below:
"""
import random

print(random.randint(-25, 25))
"""

###########################  .random()  ###########################
    Returns a pseudo-random floating-point number between 0 and 1.
The .random() method accepts no parameters and returns a pseudo-random floating-point number between 0.0 and 1.0.
Syntax
"""
random.random()
"""
Codebyte Example

It is possible to generate a pseudo-random float between 0 and a given number by multiplying it by random.random():
"""
import random

print(random.random())

print(random.random() * 10.0)
"""

###########################  .randrange()  ###########################
    Selects a random number from a defined range of int values.

The .randrange() method selects a random number from a defined range of int values.
Syntax
"""
random.randrange(start, stop, step)
"""
Example

Here, .randrange() is used to return a random number between 0 and 99:
"""
import random

print(random.randrange(0, 100))
"""
Codebyte Example

In the example below, .randrange() is used to return a random number that is between 0 and 99 and divisible by 5:
"""
import random

print(random.randrange(0, 100, 5))
"""

###########################  .sample()  ###########################
    Returns a list of items randomly selected from a given population.
###########################  .seed()  ###########################
    Initializes a pseudo-random number generator with a seeded value and sets the first number.
###########################  .shuffle()  ###########################
    Takes a list and randomly re-orders the items.
###########################  .uniform()  ###########################
    Returns a pseudo-random floating-point number between two given numbers.

Interested in helping build Docs? Read the Contribution Guide or share your thoughts in this feedback form.
Edit on GitHub

"""
