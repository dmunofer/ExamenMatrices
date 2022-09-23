

def ejercicio1(matriz):

    for e in range(len(matriz)):
        if matriz[e][3]==sum((matriz[e][0],matriz[e][1],matriz[e][2])):
            pass
        else:
            matriz[e][3]=sum((matriz[e][0],matriz[e][1],matriz[e][2]))

    return matriz