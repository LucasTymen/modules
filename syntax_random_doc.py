"""
https://www.codecademy.com/resources/docs/python/random-module

    Docs/
    Python/
    Random Module

Random Module

In Python, the built-in random module is used to randomly generate numbers as well as randomly manipulate collections
such as lists and strings.

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
The .randint() method returns a random integer that exists between two int values, int_a and int_b (inclusive), passed
as arguments.
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

The .sample() method returns a list of items that are randomly sampled from a given population. The returned list
consists of randomly selected items without duplicates.
Syntax

For arguments, the .sample() method accepts a population and a number to set the length of the returned sample.
syntax :
"""
random.sample(population, number)
"""
The population is a sequence of items can either be a list, string, or range. If sets are used, they should be converted
to a list or tuple before being passed to this method.
Codebyte Example
"""
import random

my_range = range(1000)

my_sample = random.sample(my_range,10)

print(my_sample)
"""

###########################  .seed()  ###########################
    Initializes a pseudo-random number generator with a seeded value and sets the first number.

In the Python random module, the .seed() method is used to create a pseudo-random number generator. Pseudo-random number
generators appear to produce random numbers by performing some operation on a value. This value is the seed and it sets
the first “random” value of the number sequence. With seeds, a user is able to reproduce the same pseudo-random numbers
multiple times.
Syntax

The .seed() method sets the first random number of the generator, either with a value or without one:
"""
random.seed(value)
random.seed()
"""
The value can be an int, float, str, byte, bytearray, or NoneType. If one is not provied, the random number generator
will use the current system time to create the seed.
Example

In most cases, the .seed() method uses the current time of the computer’s system to initialize a new generator:
"""
import random

random.seed()

print(random.random())
"""

Codebyte Example

In the example below, the .seed() method is used three times, once with no value and the other two with the same value
of 5. In the output, each call to random.seed(5) guarantees the first pseudo-random value from the output will be the
same every time:
"""
import random

random.seed()
print(random.random())

random.seed(5)
print(random.random())

random.seed(5)
print(random.random())
"""

###########################  .shuffle()  ###########################
    Takes a list and randomly re-orders the items.

The .shuffle() method takes a list as a parameter and randomly re-orders the contents in place.
Syntax
"""
random.shuffle(list)
"""
The list is the collection of items to be shuffled in place.
Example

After importing the random module, lists can be rearranged with .shuffle():
"""
import random

my_list = [0,1,2,3,4,5,6,7,8,9]

random.shuffle(my_list)

print(my_list)

# Output: [2, 3, 5, 0, 6, 8, 4, 7, 1, 9]
"""
Codebyte Example:
"""
import random

deck_of_cards = [
  "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
  "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
  "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
  "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
  "Joker", "Joker"
]

random.shuffle(deck_of_cards)

print(deck_of_cards)
"""

###########################  .uniform()  ###########################
    Returns a pseudo-random floating-point number between two given numbers.

The .uniform() method takes two numbers as arguments and returns a pseudo-random floating-point number between them.
The result is inclusive of the first value, and possibly inclusive of the second value, depending on rounding.
Syntax
"""
random.uniform(value1, value2)
"""
Where value1 and value2 are numbers bounding the choice of a random floating-point number.
Example

In the example below, .uniform() is used to return a random floating-point number between 10 and 20:
"""
import random

print(random.uniform(10,20))
"""
Example output:

13.188312896316244

Codebyte Example

The following example prints random floating-point numbers between 10 and 15, 100 and 150, -10 and 10, and 0.75 and 0.90.
"""
import random

print(random.uniform(10,15))
print(random.uniform(100,150))
print(random.uniform(-10,10))
print(random.uniform(0.75,0.90))
"""
Interested in helping build Docs? Read the Contribution Guide or share your thoughts in this feedback form.
Edit on GitHub

"""

###########################  .Decimal()  ###########################
# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)


########################### Aliasing with ‘as’ keyword ###########################

# Aliasing matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.plot(x, y)

# Aliasing calendar as c
import calendar as c
print(c.month_name[1])
