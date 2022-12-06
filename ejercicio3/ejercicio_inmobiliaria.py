import math

"""
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
[
{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:
Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
"""
lista = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
    ]

def inmuebles(lista): 
    for elem in lista:
        precio = (elem['metros'] * 1000 + elem['habitaciones'] * 5000 + elem['garaje'] * 15000 )* (2022 - (elem['año']))/100
        if elem['zona'] == 'A':
            elem['precio'] =  math.trunc(precio)
        elif elem['zona'] == 'B':
            elem['precio']  = math.trunc(precio * 1.5)
    return lista


def precios(lista, presupuesto):
    filtro = list(filter(lambda elem: elem['precio'] <= presupuesto, lista))    
    return filtro


print (" ---- INMUEBLES ----")
result = (inmuebles(lista))
print(result)
presupuesto = int((input("Introduce el presupuesto: ")))
print ("----- BÚSQUEDA PRECIOS------")
result_filter = precios(lista, presupuesto) 
print (list((result_filter)))