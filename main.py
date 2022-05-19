# Key Libraries
import re

# Project #1: 
def exp(amt, exp, time):
  print((amt * exp) ** time) 

amount = float(input())
exponent = int(input())
days = float(input())

print(amount, exponent, days)

# Project #2:
def addition(a, b):
  print(a + b)

x = int(input())
y = int(input())
print(x + y)

# Project #3: FizzBuzz
def fizzbuzz(num):
  for x in range(1, num, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

n = int(input())
print(fizzbuzz(n))

# Project #4: Celsius to Fahrenheit

def conv(c):
  f = ((9 / 5) * c) + 32  
  return f
 
celsius = int(input())
print(conv(celsius))

# Project #5: Book Titles
file = open("/usercode/files/books.txt", "r")
def book_titles(file):
  for line in file:
    if line[-1] == "\n":
      print(line[0] + str(len(line) - 1))
    else:
      print(line[0] + str(len(line)))
  file.close()

book_titles(file)

# Project #6: Longest Word
def longest_word():
  text = input().split()
  length = [len(x) for x in text]
  maximum = max(length)
  text_index = length.index(maximum)
  print(text[text_index])

print(longest_word())

# Project #7: Fibonacci
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_fib(numbers):
  for number in range(numbers):
    print(fibonacci(number))
  
nums = int(input())
print_fib(nums)

# Project #8: Juice Maker
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    
    def __add__(self,newJuice):
        
        self.name += "&" + str(newJuice.name)
        self.capacity += newJuice.capacity 
        return self.__str__


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)


print(a.__add__(b)())

# Project #9: Phone Number Validator
def phone_valid():
  num = input()
  pattern = r"^[1|8|9][0-9]*$"
  if re.match(pattern,num) and len(num) == 8:
      print("Valid")
  else:
      print("Invalid")

print(phone_valid())

# Project #10: Adding Words
def concat(*args):
  return '-'.join(args)

print(concat("I", "love", "Python", "!"))
