def say_hello(name):
     print("Hola, mi nombre es " + name)

def where_from(place):
     print("Yo soy de " + place)

def oration(name, place):
    say_hello(name)
    where_from(place)

places = ["Mexico", "Honduras", "Espana", "Filipinas", "Cuba"]
names = ["Miguelito", "Jose", "Ricarda", "Juliana", "Carolina"]

for name in names:
    for place in places:
        oration(name, place)
