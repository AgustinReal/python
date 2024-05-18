"""
polidromos 

radar
atar a la rata
"""


def palindromo(str_input):
    str_origal = str_input.replace(" ", "")
    str_revero = str_input[::-1].replace(" ", "")

    if(str_origal == str_revero):
        print(" es un palindromo")
    else:
        print(" No es palindromo")


if __name__ == "__main__":
    str_input = input("Ingrese una frase : ")
    palindromo(str_input=str_input)
    input(str_input)