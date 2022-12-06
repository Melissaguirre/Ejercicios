#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def cadena(words: str):
    words = words.split()
    dicc= {}
    for word in words:
        if word in dicc:
            dicc[word] += 1
        else:
           dicc[word] = 1                
        
    return dicc

def repetidos(dicc):
        mayor = 0 
        tupla = ()
        for clave, valor in dicc.items():
            if valor > mayor :
                mayor = valor    
                tupla = (clave, mayor)
        return tupla      
 
     
               
words = (input("Ingresa una cadena: "))
print (cadena(words))  
print (repetidos(cadena(words)))           
 
