
#ARGS
# def func(*args):
#     #return n1 + n2 + n3 + n4 + n5 + n6
#     for item in args:
#         print(item)
    

# func("agus","hola mundo", 1, 2, 3, 4, 5, 6, 8, 9, 7, 11)

#KARGS
days ={
    "dia1" : "Lunes",
    "dia2" : "Martes"
}

# def func2(**kargs):
#     print(kargs)

# func2(**days)# a la hora de pasarle los parametros, si un dic, se le paso con ** => **[nombre del dic]

def func3(*args, **kargs):
    print(args)
    print(kargs)

func3(1, 2, 3, 4, 5, 6, 7, **days)