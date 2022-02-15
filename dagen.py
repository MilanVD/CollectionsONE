dagen = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']

print('Alle dagen: ')
for i in range(7):
    print(dagen[i])
print('De werkdagen: ')
for i in range(5):
    print(dagen[i])
print('De weekenddagen: ')
for i in (5, 6):
    print(dagen[i])
print('Alle dagen omgekeerd: ')
for i in range(6, -1, -1):
    print(dagen[i])
print('werkdagenmgekeerde: ')
for i in range(4, -1, -1):
    print(dagen[i])
print('weekenddagen omgekeerd : ')
for i in range(6, 4, -1):
    print(dagen[i])

