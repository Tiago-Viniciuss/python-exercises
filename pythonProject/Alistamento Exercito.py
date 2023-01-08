resposta = int(input("Qual o ano do seu nascimento? "))
anoatual = 2022
idadealuno = anoatual - resposta
idadeideal = 18
multa = 200
if idadealuno < idadeideal:
    print (f"Você ainda não tem 18 anos, retorne daqui a {idadeideal - idadealuno} anos.")
elif idadealuno > idadeideal:
    print (f"O prazo para se alistar já passou há {idadealuno-idadeideal} anos! Você receberá uma multa no valor de { (idadealuno-idadeideal)*multa}!")
else:
    print ("Muito bem, Recruta! Está na hora de se alistar!")    