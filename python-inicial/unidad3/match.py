"""
match => Sirve para evaluar un dato y con base a ello realizar una acción.
"""

status = "liquido"

match status: # Valor
    case "solido":# condición == valor (status == "solido")
        print("El estado es solido")
    case "liquido":# condición == valor (status == "liquido")
        print("El estado es liquido")
    case "gaseoso":# condición == valor (status == "gaseoso")
        print("El estado es gaseoso")
    case _:# Default => Caso especial, cuando no cumple con ningun case anterior.
        print("El estado no existe")

status = "liquido"

match status: # Valor
    case "solido" | "liquido" | "gaseoso":# condición triple: solido o liquido o gaseoso
        print("El estado es solido o liquido o gaseoso")
    case "plasmatico":# condición == valor (status == "plasmatico")
        print("El estado es plasmatico")
    case _:# Default => Caso especial, cuando no cumple con ningun case anterior.
        print("El estado no existe")

status = "liquido"

match status: # Valor 
    case "solido" | "liquido":# condición doble: solido o liquido 
        print("El estado es solido o liquido")
    case "plasmatico":# condición == valor (status == "plasmatico")
        print("El estado es plasmatico")
    case _:# Default => Caso especial, cuando no cumple con ningun case anterior.
        print("El estado no existe")