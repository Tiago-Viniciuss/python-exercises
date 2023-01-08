import random
aleatorio = random.randint(0,5)
escolha = int(input("Escolha um número aleatório entre 0 e 5: "))
print (aleatorio)
if escolha == aleatorio:
    print ("Caralho! Você acertou!")
else:
    print ("Putz... Falta de sorte!")    