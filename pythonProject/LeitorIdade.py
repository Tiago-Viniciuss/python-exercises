from datetime import date
atual = date.today().year
print (">>>C.N.N.<<<")
nasc = int(input("Em que ano você nasceu? "))
idade = atual - nasc
if idade <= 9:
    print (f"Já que você tem {idade} anos, sua categoria é MIRIM.")
elif idade > 9 and idade <= 14:
    print (f"Já que você tem {idade} anos, sua categoria é INFANTIL.")
elif idade > 14 and idade <= 19:
    print (f"Já que você tem {idade} anos, sua categoria é JUNIOR.")
elif idade == 20:
    print (f"Já que você tem {idade} anos, sua categoria é SÊNIOR.")
else:
    print (f"Já que você tem {idade} anos, sua categoria é MASTER.")                 