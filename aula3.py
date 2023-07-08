

cotacao_dolar = 4.87

cotacao_alvo = 5.04

validar_cotacao = cotacao_dolar<cotacao_alvo

print("Cotação do Dolar é Menor que 5,04?",validar_cotacao,"O valor atual é",cotacao_dolar)

#Comparacao
#Fazer uma comparação e informar se a cotação do dolar é menor ou maior

#Funções e métodos
texto = "Cotação do Dolar"
texto = texto.replace("Dolar","Dólar")
print(texto)
texto = texto.upper()
print(texto)

nome = "pablito"
prefixo = nome[:3]
print(prefixo)

sufixo = nome[-3:]
print(sufixo)

meio = nome[3:5]
print(meio)

#Imagine que você seja o comprador da sua empresa e durante a licitação você precisa avaliar alguns pontos
#para que você possa realizar a compra com o melhor custo beneficio
#Neste momento voce esta gerenciando uma licitação de compra de leite e as regras para identificar
#O melhor custo beneficio são: 
# O litro do leite tem que ser inferior a 7 reais
# 2 O prazo de validade tem que ser superior a 6 meses
#Suponha que você recebeu as seguintes propostas

#Empresa 1
# Litro do Leite = R$ 7,50
# Validade: 12 meses

#Empresa 2
#Litro = R$ 6,99
#Validade: 3 meses

#Empresa 3
#Litro = R$ 6,00
#Validade: 3 meses
#Desenvolver um pequeno algoritmo onde seja possível identificar a Empresa Vencedora.
#Sabendo que, os seus testes lógicos precisam retornar como "verdadeiro" para ambos (litro e validade)

leite_ideal = 7
validade_ideal = 6 


empresa1_leite = 7.5
empresa1_validade = 12
validador1 = empresa1_leite < leite_ideal  and empresa1_validade > validade_ideal

print("Empresa 1",validador1)

empresa2_leite = 6.9
empresa2_validade = 3
validador2 = empresa2_leite < leite_ideal  and empresa2_validade > validade_ideal 

print("Empresa 2",validador2)
empresa3_leite = 6
empresa3_validade = 7
validador3 = empresa3_leite < leite_ideal and empresa3_validade > validade_ideal
print("Empresa 3",validador3)

print("A Empresa vencedora é a Empresa 2 com Valor do Litro a",empresa2_leite, "E a validade ",empresa2_validade)

namorada = "jessica"

prefixo_2=namorada[:4]
print(prefixo_2)





