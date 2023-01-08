peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura*altura)
if imc <= 18.5:
    print (f"Seu IMC é {round(imc,2)}, portanto, você está abaixo do peso!")
elif imc > 18.5 and imc <= 25:
    print (f"Seu IMC é {round(imc,2)}, portanto, você está no peso ideal!")
elif imc > 25 and imc <= 30:
    print (f"Seu IMC é {round(imc,2)}, portanto, você está com sobrepeso!")    
elif imc > 30 and imc <= 40:
    print (f"Seu IMC é {round(imc,2)}, portanto, você está obeso!")
else:
    print (f"Seu IMC é {round(imc,2)}, portanto, você está com obesidade mórbida!")    
