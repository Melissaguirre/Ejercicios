def anio_bisiesto(anio):
    if anio % 4 == 0 and anio % 400 == 0 and anio % 100 == 0:
        print ("Es un año bisiesto.") 
    elif anio % 4 == 0 and anio % 400 == 0 and anio % 100 != 0:
        print ("Es un año bisiesto.")
    elif anio % 4 == 0 and anio % 400 != 0 and anio % 100 == 0:
        print ("No es un año bisiesto.")
    elif anio % 4 != 0 and anio % 400 != 0 and anio % 100 != 0:
        print ("No es un año bisiesto.")
        

anio = (input("Ingresa un año: "))
print (anio_bisiesto(anio))