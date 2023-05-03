"""

Modules in Python
Modules Python Decimals

Let’s say you are writing software that handles monetary transactions. If you used Python’s built-in floating-point
arithmetic to calculate a sum, it would result in a weirdly formatted number.
"""
cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996

"""
Being familiar with rounding errors in floating-point arithmetic you want to use a data type that performs decimal
arithmetic more accurately. You could do the following:
"""
from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

"""
Above, we use the decimal module’s Decimal data type to add 0.10 with 0.35. Since we used the Decimal type the
arithmetic acts much more as expected.

Usually, modules will provide functions or data types that we can then use to solve a general problem, allowing us more
time to focus on the software that we are building to solve a more specific problem.

Ready, set, fix some floating point math by using decimals!
Instructions
1.

Run your code to see the weird floating point math that occurs.
2.

In script.py import Decimal from the decimal module.
3.

Use Decimal to make two_decimal_points only have two decimals points and four_decimal_points to only have four decimal
points.

The number of decimal points will adjust to the correct number when you use Decimal as shown in the example.

Make sure to use quotes around the floats. Each number will need to be converted with Decimal BEFORE performing the
operations.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can we perform calculations between Decimal objects and other values?

How can we control the rounding of our equation?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
