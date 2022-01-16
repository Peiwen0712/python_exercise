
'''
Question 1: 
 
 Adapt the “HelloWorld” code below to produce a program that defines a variable capable of holding an integer of your choice. The program should add 3 to that number, multiply the result by 2, subtract 4, subtract twice the original number, add 3, then print the result and a new line.
'''
 
def printHelloWorld():
  initial = 2
  initial = (((2 *(initial + 3)) - 4) - (initial * 2)) + 3
  print("Result = " , initial)

print("Question 1\n")
printHelloWorld()

##################################################################

'''
Question 2: 
 
 Complete the function below so that it prints every integer from x to x + 10.  Do not use loops. 
 
 Call this function from the main to test your program.
'''

def printXTenTimes():
  for i in range(10):
    print(i+1)

print("\nQuestion 2\n")
printXTenTimes()

##################################################################

'''
Question 3: 
 
 Complete the function below so that it converts the height of a person from centimetres to feet and inches. Use integer division (rounding down is acceptable, which is the default for integer division). 
 
 Hint: 254 cm is exactly 100 inches and 12 inches is exactly 1 foot. 
 
 Call this function from the main to test your program.  For example you could test your program with the follow five values, where "?" replaced with the true value.

 101 cm is 3 feet 3 inches to the nearest inch.
 3 cm is 0 feet 1 inches to the nearest inch.
 15 cm is ? feet ? inches to the nearest inch.
 192 cm is ? feet ? inches to the nearest inch.
 124 cm is ? feet ? inches to the nearest inch.
'''

def convertMetricToImperialHeights(cm):
  inch = cm / 2.58
  feet = inch // 12
  inch = inch % 12
  print(cm," cm is ", round(feet) ," feet ", round(inch) , "inches to the nearest inch.")

print("\nQuestion 3\n")
convertMetricToImperialHeights(15)
convertMetricToImperialHeights(192)
convertMetricToImperialHeights(124)

##################################################################

'''
Question 4: 
 
 Complete the function below so that it uses three variables (current, previous, next) to calculate and print out the first ten numbers of the Fibonacci sequence, each on a new line: i.e. the first four lines should be as follows:

 0 
 1 
 1 
 2
 
'''

def fibonacci():
  n0 = 0
  n1 = 1
  count = 0
  while count < 10:
        print(n0)
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        count += 1    

print("\nQuestion 4\n")
fibonacci()

##################################################################

'''
 Question 5: 
 
 Complete the function below so that it uses two variables: height and radius. Use these two variables and print to the screen, the volume of a cylinder. 

 Call this function from the main to test your program.  For example, you could test your program with the following values, 

 height 7.0cm and radius 4.0cm
 height 20.0cm and radius 3.0cm
 height 14.7cm and radius 5.2cm
 
 Which prints out, 
 
 the cylinder with height 7.0cm and radius 4.0cm has a volume of 351.86cm^3

'''
def volumeOfACylinder(r=4, h=7):
  height = '7.0cm'
  radius = '4.0cm'
  print(f"the cylinder with {height}  and {radius} has a volume of ",(3.14 * r * r * h)," cm^3")

def volumeOfACylinder2(r=3, h=20):
  height2 = '20.0cm'
  radius2 = '3.0cm'
  print(f"the cylinder with {height2}  and {radius2} has a volume of ",(3.14 * r * r * h)," cm^3")

print("\nQuestion 5\n")
volumeOfACylinder()
volumeOfACylinder2()
