'''
Task
Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer,  (the argument to pass to factorial).

Output Format

Print a single integer denoting integer!.
'''

#! /usr/bin/python

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(raw_input().strip())
print factorial(n)

