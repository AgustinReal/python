# if
# condicion = (if) true => ejecuta codigo
# condicion = (else) false => ejecuto otra poción de codigo

edad_persona = int(input("Ingrese su edad por favor: "))
EDAD_BASE = 18 # edad auxiliar para comparar con la ingresada por el usuario.

if edad_persona > EDAD_BASE: # Si el usuario ingresa una edad mayor a 18 "entra aqui!!".
    print("Eres mayor de edad y mayor a 18 años")
    if edad_persona == 50: # Si el usuario ingresa una edad igual a 50 "entra aqui!!".
        print("Tienes 50 años de edad")
elif edad_persona == 18: # Si el usuario ingresa una edad igual a 18 "entra aqui!!".
    print("Tienes 18 años de edad")
else:# Si el usuario ingresa una edad menor a 18 "entra aqui!!".
    print("Eres menor de edad")
    
              