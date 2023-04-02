""" crie um progama em python que pergunte km rodado dias de  uso do veiculo 
considere 60 reais por dia com o veiculo e 0.15 reias por kilometro rodado 
exiba quanto custara o alugek do carro"""
distancia = float(input("informe a distacia pecorrida em (km):"))
qtd_dias = float(input("informe quntos dias permanceu com o veiculo:"))
valor_pago = distancia * 0.15 + qtd_dias * 60
print("o valor pago pelo alugel sera: {:.2f} reais".format(valor_pago))
