#Nesesito crear una funcion que compare  dos cadenas de strings y ordenar los elementos de 
#esas cadenas alfabeticamente  y que s elisten en un dicionario

def comparar_cadenas_lexicograficas(cadena1,cadena2):
    #si la cadena1 es menor que la segunda retornar "-1"
    if cadena1<cadena2 :
        return -1
    elif cadena1 > cadena2:
        return 1
    else:
        return 0
    
print(comparar_cadenas_lexicograficas(['abc'], ['abd']))

        