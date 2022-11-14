# Turimas sąrašas, pvz.:

# canvas = [
#   "abc",
#   "ded"
# ]

# Sukurkite funkciją "addFrame", kuri pridėtų rėmelį ir grąžintų pamodifikuotą sąrašą:

# canvas_with_frame = [
#   "*****"
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

# Pastaba: sąrašas gali ir neturėti nei vieno elemento arba turėtų tusčių elementų. pvz.
# canvas = [] arba canvas = [""]

# Jeigu sąrašas yra tusčias arba visi elementą tušti išmeskite klaidą - "Error: empty canvas provided".
# Beje, sąraše esantis tekstas, gali būti ir skirtingo ilgio. Todėl rėmelis turėtų būti brėžiamas pagal ilgiausią saraše esantį elementą.



canvas = [
  "aaa",
  "abcddd"  
]

framed_picture = []
def addFrame(canvas):
  is_empty_str = list(filter(None, canvas))
  if not is_empty_str:
    print("Error: empty canvas provided")
 
  else:
    longest = max(len(x) for x in is_empty_str)
    for a in is_empty_str:
      framed_picture.append("*" * longest + 2 * "*")
      for a in is_empty_str:
        short = longest - len(a)
        framed_picture.append("*"+ a + " " * short + "*")
      framed_picture.append("*" * longest + 2 * "*")
      break
    return framed_picture

addFrame(canvas)
print(*framed_picture, sep="\n")


    