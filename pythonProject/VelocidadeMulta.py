velocidade = int(input ("A que velocidade o seu carro está?  "))
multa = (velocidade - 80)*7
if velocidade <=80:
    print ("Ótimo, está DENTRO do limite permitido!")   
if velocidade >80:
    print (f"Você está ACIMA do limite permitido e sua multa é de {multa} euros!")  
      