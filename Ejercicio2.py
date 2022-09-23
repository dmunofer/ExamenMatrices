
def ejercicio2():
    cadena= input('Introduce una cadena de caracteres:')
    if len(cadena)>=3 and len(cadena)<10:
        return True
    else:
        return False


cont=0
cadena= input('Introduce una cadena de caracteres:')
def ejercicio2_rec():
    final = True
    if len(cadena)<3 or cont>3:
        final = False
        list(cadena).remove(cadena[0])
        list(cadena).remove(cadena[1])
        list(cadena).remove(cadena[2])
        str(cadena)
    return ejercicio2_rec(), final
    