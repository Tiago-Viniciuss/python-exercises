#Calculando aumento de salário com 10% e 15%
question = float(input("Digite seu salário: "))
if question > 1250:
    print (f"O seu novo salário  {question + question * 10 / 100:}0€")
if question <= 1250:
    print (f"O seu aumento novo salário {question+ question * 15 / 100}0€")   