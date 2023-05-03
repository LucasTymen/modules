load_file_in_context("library.py")

try:
  if always_three() != 3:
    fail_tests("Does `always_three()` return 3?")
except NameError:
  fail_tests("Did you define a function `always_three()`?")

pass_tests()
