"""Recursion
Recursion is when a function calls itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result"""
# A simple recursive function that counts down from 5:

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
"""Basic Recursion Structure

Base case

Recursive call

Stack memory understanding"""
def print_n(n):
    if n == 0:
        return
    print_n(n-1)
    print(n)

print_n(5)
# fib
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
# palin
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))