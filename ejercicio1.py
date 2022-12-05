#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def cadena(words):
     dictionary= {}
     for word in words:
        dictionary[word] = words.count(word)
        
     return dictionary

def repetidos(texto):
        tupla = ()
        dictionary = cadena(texto)
        word_max = max(dictionary, key = dictionary.get)        #por medio del max, key y get retorna la palabra que más se repite
        repet = dictionary[word_max]                   #traer lo que tiene la key 
        tupla = (word_max, repet)
        return tupla      
 
     
               
words = (input("Ingresa una cadena: ").split())
print (cadena(words))  
print (repetidos(words))           
 
