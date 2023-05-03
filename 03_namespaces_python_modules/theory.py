"""

Modules in Python
Modules Python Namespaces

Notice that when we want to invoke the randint() function we call random.randint(). This is default behavior where
Python offers a namespace for the module. A namespace isolates the functions, classes, and variables defined in the
module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or
lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

Fortunately, this name can be altered by aliasing using the as keyword:
"""
import module_name as name_you_pick_for_the_module
"""
Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one
of its functions is laborious.

You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything. This
syntax is considered dangerous because it could pollute our local namespace. Pollution occurs when the same name could
apply to two possible things. For example, if you happen to have a function floor() focused on floor tiles, using from
math import * would also import a function floor() that rounds down floats.

Let’s combine your knowledge of the random library with another fun library called matplotlib, which allows you to plot
your Python code in 2D.

You’ll use a new random function random.sample() that takes a range and a number as its arguments. It will return the
specified number of random numbers from that range.
"""
#random.sample takes a list and randomly selects k items from it
new_list = random.sample(list, k)
#for example:
nums = [1, 2, 3, 4, 5]
sample_nums = random.sample(nums, 3)
print(sample_nums) # 2, 5, 1²
"""
Instructions
1.

Below import codecademylib3_seaborn, import pyplot from the module matplotlib with the alias plt.

The import statement will use this format:

from module_name import object_name as name_you_pick

2.

Import random below the other import statements. It’s best to keep all imports at the top of your file.
3.

Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive).
4.

Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).

Feel free to print numbers_b to see your random sample of numbers.
5.

Now let’s plot these number sets against each other using plt. Call plt.plot() with your two variables as its arguments.
6.

Now call plt.show() and run your code!

You should see a graph of random numbers displayed. You’ve used two Python modules to accomplish this (random and matplotlib).
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
