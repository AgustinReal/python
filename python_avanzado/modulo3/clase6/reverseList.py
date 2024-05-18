"""
2. given a list of strings, write a function that prints a reverse version of each string:

for example:
>a = ["Hello worrd", "Hello Python, "1 2 3 4 5 6 7 8"]
>magic_function(a)
['dlroE olleH', 'nohtyP elloH', '8 7 6 5 4 3 2 1']
"""

#froma chill
def magic_function(list_input):
    list_input = []
    for a in list_input:
        list_input.append(a[::-1])
    return list_input

#Forma pro
def magic_function(list_input):
    list_input = [a[::-1] for a in list_input]
    return list_input

a = ["Hello worrd", "Hello Python" , " 1 2 3 4 5 6 7 8" ]
b = magic_function(a)

print(b)