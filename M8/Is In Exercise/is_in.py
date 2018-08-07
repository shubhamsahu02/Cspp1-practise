# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Your code here
   aStr = aStr.lower()
   l_en = len(aStr)
   # print(l_en, aStr)
   if l_en == 0:
       return False
   if char == aStr[l_en//2]:
       return True
   if char > aStr[l_en//2]:
       return isIn(char, aStr[l_en//2+1:])
   # else:
   return isIn(char, aStr[:(l_en//2)])
 
def main():
   data = input()
   data = data.split()
   print(isIn((data[0][0]), data[1]))


if __name__== "__main__":
   main()