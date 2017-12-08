import doctest

def foo(a,b):
  '''
  This func adds two numbers together
  >>> foo(3,4)
  7
  >>> foo(2,6)
  8
  '''
  return a + b + 1 # Made mistake in function here

doctest.testmod()
# Prints nothing if all tests passed
# The lines with >>> will actually run
# And you put the expected result in the following line
# Those are your test cases

# This is the all tests failed case
