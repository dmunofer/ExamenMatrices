

def del_1_al_10():
    lista=[]
    for i in range(0,11):
        lista.append(i)
    return lista


def del_menos10_al_0():
    lista=[]
    for i in range(-10,1):
        lista.append(i)
    return lista

def pares0_al_10():
    lista=[]
    for i in range(0,21,2):
        lista.append(i)
    return lista

def del_menos20_al_0_impares():
    lista=[]
    for i in range(-21,0,2):
        lista.append(i)
    lista.remove(lista[0])
    return lista

def del_0_al_50_multiples():
    lista=[]
    for i in range(0,51,5):
        lista.append(i)
    return lista





