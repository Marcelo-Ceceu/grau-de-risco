# Algoritimo 001: primitivos e identificadores
# Dev: Marcelo Wilker
# Data: 08.09.2023

Idade = int (input("Escreva sua Idade: "))
Peso = float (input("Digite o seu Peso: "))

if Idade < 20 and Peso <=60:
    print ("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 9")
elif Idade < 20 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 8")
elif Idade < 20 and Peso < 90:

    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 7")
elif Idade >= 20 and Idade <= 50 and Peso <= 60:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 6")
elif Idade >= 20 and Idade <= 50 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 5")
elif Idade >= 20 and Idade <= 50 and Peso > 90:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 4")

elif Idade > 50 and Peso <= 60:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 3")
elif Idade > 50 and Peso > 60 and Peso <= 90:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 2")
elif Idade > 50 and Peso > 90:
    print("Com", Idade, "anos e peso de ", Peso, "Kilos, você esta no grau de risco 1")
