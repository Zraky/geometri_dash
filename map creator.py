import random
"""m = []

# Ajouter 9 sous-listes à m
for x in range(9):
    m.append([])
    for i in range(200):
        m[x].append(0)

m.append([])
# Ajouter 200 éléments supplémentaires à m
for i in range(200):
    m[-1].append(1)

for y in range(len(m)):
    print(m[y])"""

m = [0]



for i in range(200):
     x = random.randint(0, 10)
     if m[-1] == 1:
         y = random.randint(1, 10)
         if y < 6:
             m.append(1)

         else:
             m.append(0)
     elif x < 1:
         m.append(1)

     else:
         m.append(0)


print(m)
