import json
from difflib import get_close_matches

data= json.load(open("palabras.json"))

def significado(x):

    if x in data:
        return data[x]
    
    elif len(get_close_matches(x, data.keys())) > 0: 
        
        concidencia= get_close_matches(x, data.keys()) [0]
    
        print("Quieres decir:", concidencia)
        print("Si es correctar presiona (Y) si no presiona (N) ")
        respuesta = input()
    
        if respuesta.lower() == "y":
            return(data[concidencia])
        
        elif respuesta.lower()== "n":
            return("No se que palabra es quieres buscar")
        
        
    else:
        return("La palabra no existe,ingrese otra palabra")


palabra= input("Ingrese una palabra :\n").lower()

k= significado(palabra)

if type(k) == list:
    for item in k:
         print(item)
else:
    print(k)    
  