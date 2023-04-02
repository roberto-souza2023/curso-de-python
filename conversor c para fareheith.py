""" escreva um codigo em python que aparti de uma temperatura em graus c°
seja convertida graus f°"""
celsius = float(input("informe a temperatra atual (celsius): "))
fahrenheit = 9* celsius / 5 + 32
print(" a temperatura {} C° coresponde {}F°"
.format(celsius, fahrenheit))
