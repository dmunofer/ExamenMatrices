

def tabla():
    a= input('Introduce el primer argumento entre 1 y 9:')
    b= input('Introduce el segundo argumento entre 1 y 9:')
    if int(a)<=1 or int(a)>=9 or int(b)<=1 or int(b)>=9:
        raise Exception('Error. Los argumentos deben ser números enteros entre el 1 y el 9')

    for i in range(0,int(a)):
        print('')
        for e in range(0,int(b)):
            print('*',end='')


