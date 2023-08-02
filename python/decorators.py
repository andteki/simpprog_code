

def valami1(funkcio):
    def belso():
        print("Dekoráció kezdete")
        funkcio()
        print("Dekoráció vége")
    return belso

# A dekorálás
@valami1
def udvozles():
    print("Helló")

# Az eredeti függvény meghívása
udvozles()
