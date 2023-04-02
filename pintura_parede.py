""" escreva um codigo em python que aparti da altura e largura em metros 
indetifique quanto de tinta  e necessaria na pintura considere 1l=2(m2)"""
largura = float(input("informe a largura da parede: "))
altura = float(input("informe a alatura da parede: "))
area = largura * altura
volume = area / 2 
print("o volume necessario para pintar uma parede de {:.2f}m2 e {:.2f} litros"
.format(area, volume))