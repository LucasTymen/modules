load_file_in_context("script.py")

try:
  always_three()
except NameError:
  fail_tests("Did you import `library`?")

pass_tests()
