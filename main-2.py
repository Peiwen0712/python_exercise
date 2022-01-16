
''' 
 Write a function which returns true if a number is divisible by 3 and  false if it is not.  Hint: use the modulo (%) operator.

 Modify your code so that your function now returns true if a number is divisible by 3 or 5 and false if it is not.
'''

def mod3(number):
  return bool(number%3 == 0)

print(str(mod3(15)))
print(str(mod3(20)))

def mod3mod5(number):
  return bool(number%3 == 0 ) or  bool(number%5 == 0)
print(str(mod3(15)))
print(str(mod3(20)))
print(str(mod3(22)))