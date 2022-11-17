# Sukurkite funkciją "addDigits", kuri priims sveiką skaičių nuo 10 iki 999 ir grąžins jo skaitmenų sumą. 

# Pvz.
# Jeigu duota 34, funckiją turėtų grąžinti 7.
# Jeigu duota 999, funckija turėtų grąžinti 27.

import random

def addDigits(number):
  result = 0
  for element in str(number):
    result += int(element)
  return result

number = random.randint(10,999)
print("Skaicius: " , number)
print("Suma: " , addDigits(number))
