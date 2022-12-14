"""
Escribir una clase en python que encuentre los 3 elementos que sumen 0 a partir de números reales
Entrada: [-25, -10, -7, -3, 2, 4, 8, 10]
Salida: [[-10, 2, 8], [-7, -3, 10]]
"""

lista = [-25, -10, -7, -3, 2, 4, 8, 10]

def sum_numbers(lista):
    lista_final = []
    for elem1 in lista[:3]:
        for elem2 in lista[3:6]:
            for elem3 in lista[6:]:
              suma = elem1 + elem2 + elem3 
              if suma == 0:
                lista_final.append(elem1)
                lista_final.append(elem2)
                lista_final.append(elem3)
                
    return lista_final[:3],lista_final[3:]

result = (sum_numbers(lista))
print (list(result))