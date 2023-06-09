"""
Modules in Python
Modules Python Introduction

In the world of programming, we care a lot about making code reusable. In most cases, we write code so that it can be
reusable for ourselves. But sometimes we share code that’s helpful across a broad range of situations.

In this lesson, we’ll explore how to use tools other people have built in Python that are not included automatically for
you when you install Python. Python allows us to package code into files or sets of files called modules.
==>>  https://www.codecademy.com/resources/docs/python/modules?page_ref=catalog

A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred
to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

Usually, to use a module in a file, the basic syntax you need at the top of that file is:
"""
from module_name import object_name
"""
Often, a library will include a lot of code that you don’t need that may slow down your program or conflict with
existing code. Because of this, it makes sense to only import what you need.

One common library that comes as part of the Python Standard Library is datetime. datetime helps you work with dates and
times in Python.
==>> https://www.codecademy.com/resources/docs/python/dates?page_ref=catalog

Let’s get started by importing and using the datetime module. In this case, you’ll notice that datetime is both the name
of the library and the name of the object that you are importing.
Instructions
1.

In script.py import the datetime type from the datetime library.
2.

Create a variable current_time and set it equal to datetime.now().
3.

Print out current_time.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    How can we see all the objects and functions in a module?

Why doesn’t datetime.now() match with the current time?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
