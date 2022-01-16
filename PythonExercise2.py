import math
'''
Question 0:

Complete the recursive function below which performs multiplication of two  numbers without using the inbuilt * sign
'''

def multiply(number, by):
  return number*by
print("Question 0:");  
print(str(multiply(2,3)))
print(str(multiply(4,3)))
print("")

##################################################################

'''
Question 1: 
 
 Complete the function below which takes in an integer input between zero and one hundred (0 ≤ n ≤ 100) and prints out the number expressed in English text, with spaces and no dashes (–), e.g. for the number “33”, we would expect to see “thirty three”. Hint: you may want to create additional functions to help.
 
 Call this function from the main to test your program.
'''

def numberToText(value):
# check if the value is in the 0 to 100
  if value not in range(0,101):
    print("Error: out of range.\n")
    return

# value between 1 and 10 or between 20 and 99
  if value in range(1,10) or value in range(20,100):
    tens = (value//10)
    units = value%10 #reminder
    return tensName(tens) + unitsName(units)
  else:
    return (special(value))

# Dictionary of numbers
def special(s): 
  special = {0:"zero", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 100:"one hundred"}
  return (special[s])

def tensName(t):
  tens = {0:"", 1:"ten", 2:"twenty ", 3:"thirty ", 4:"forty ", 5:"fifty ", 6:"sixty ", 7:"seventy ", 8:"eighty ", 9:"ninety "}
  return (tens[t])

def unitsName(u):
  units = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
  return (units[u])
print("Question 1:") 
print(numberToText(5))
print(numberToText(12))
print(numberToText(95))
print(numberToText(100))
print(numberToText(101))
print("")

##################################################################
'''
Question 2: 
 
 Complete the function below that calculates, and returns, the distance between two points.
 
 Call this function from the main to test your program. Hint: may wish to use the following print statement in your main function, or similar: 

 printf("%1.2f\n", calculateDistance(0, 0, 4, 3));
'''


def calculateDistance(x1, y1, x2, y2):
  return math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
print("Question 2") 
print(str(calculateDistance(1,0,129,1)))
print("")

##################################################################

''' 
Question 3: 
 
 Complete the function below that is given an integer, n, where 1 ≤ n ≤ 9999 and prints whether it is even, odd, or/and prime.  The output should be whole sentences for example, 

 1 is odd and not prime.
 2 is even and prime.
 3 is odd and prime.
 4 is even and not prime.
 5 is odd and prime
 
 Call this function from the main to test your program.
'''

def printOddEvenAndOrPrime(n):
# check 0  
    if (n == 0):
      return ("0 is even and not prime.")

# check 1  
    elif (n == 1):
      return("1 is odd and not prime.")

# check 2  
    elif (n == 2):
      return("2 is even and prime.")

# even numbers
    elif (n%2 == 0):
      return(n, "is even and not prime.")

# odd numbers
    else:
      for i in range(2, n):
       if (n % i) == 0:
          return (n, "is odd and not prime.")
      else:
          return (n, "is odd and prime.")

print("Question 3");  
print(printOddEvenAndOrPrime(2))
print(printOddEvenAndOrPrime(12))
print(printOddEvenAndOrPrime(13))
print(printOddEvenAndOrPrime(39))
