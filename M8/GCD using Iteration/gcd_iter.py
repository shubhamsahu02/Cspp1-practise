# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
   '''
   a, b: positive integers
   
   returns: a positive integer, the greatest common divisor of a & b.
   '''
   # Your code here
   for c in range(a*b+1, 1, -1):
       if a%c == 0 and b%c == 0:
           return c

def main():
   data = input()
   data = data.split()
   print(gcdIter(int(data[0]),int(data[1])))

if __name__== "__main__":
   main()