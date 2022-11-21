# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.



m1 = [[2,6],
      [3,3]]

m2 = [[0,1],
      [4,5]]

result = [[0 for x in range(2)] for y in range(2)]

for a in range(len(m1)):
    for b in range(len(m2[0])):
        for c in range(len(m2)):
            result[a][b] += m1[a][c] * m2[c][b]

print(result)


# Okay, čia jūs visi gana standartiškai 😄 kiek žiūrėjau dar niekas netikrino ar 
# galima iš tikrųjų sudauginti matricas.
#  O čia ir buvo kabliukas.
# Šitai funkcijai reikėtų patikrinimo ar išvis galima tokia matricas dauginti, t.y. 
# vienos matricos stulpelių skaičius būtų lygus kitus matricos eilučių skaičiui.








