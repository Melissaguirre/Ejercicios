def anio_bisiesto(anio):
    if anio % 4 == 0 and anio % 400 == 0 and anio % 100 == 0:
        msj = ("Es un año bisiesto.") 
    elif anio % 4 == 0 and anio % 400 != 0 and anio % 100 != 0:
        msj = ("Es un año bisiesto.")
    elif anio % 4 == 0 and anio % 400 != 0 and anio % 100 == 0:
        msj = ("No es un año bisiesto.")
    elif anio % 4 != 0 and anio % 400 != 0 and anio % 100 != 0:
        msj = ("No es un año bisiesto.")
        
    return msj     

anio = (input("Ingresa un año: "))
print (anio_bisiesto(anio))