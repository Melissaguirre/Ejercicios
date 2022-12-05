#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def cadena(words):
     dictionary= {}
     for word in words:
         if word in dictionary:
            dictionary[word] += 1
         else:
           dictionary[word] = 1                
        
     return dictionary

def repetidos(words):
        mayor = 0 
        tupla = ()
        dictionary = cadena(words)
        for clave, valor in dictionary.items():
            if valor > mayor :
                mayor = valor   
                tupla = (clave, mayor)
                return tupla      
 
     
               
words = (input("Ingresa una cadena: ").split())
print (cadena(words))  
print (repetidos(words)) 
 