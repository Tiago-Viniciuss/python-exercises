question = int(input("Digite seu salário: "))
if question > 1250:
    print (f"O seu aumento será de {(question/100)*10:}0€")
if question <= 1250:
    print (f"O seu aumento será de {(question/100)*15}0€")   