import sys

def hello(name):
  """Print "Hello " and a name and return None"""
  print("Hello", name)

if __name__ == '__main__':
  program = sys.argv[0]
  hello('World')
  print("Program running is:", program)