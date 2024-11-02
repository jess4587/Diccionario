import json

data= json.load(open("palabras.json"))

def significado(x):

    if x in data:
        return data[x]

    else:
        return("La palabra no existe,ingrese otra palabra")


palabra= input("Ingrese una palabra en ingles porque estamos corto de idiomas:\n").lower()

print(significado(palabra))


  