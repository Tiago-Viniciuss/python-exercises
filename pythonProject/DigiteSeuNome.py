nome = str(input("Digite seu nome completo: ")).strip()
print (f"Seu nome em maiúsculas é {nome.upper()}.")
print (f"Seu nome em minúsculas é {nome.lower()}.")
print (f"Seu nome tem {len(nome)-nome.count(' ')} letras.")
primeiro = nome.split()
print (f"Seu primeiro nome é {primeiro[0]}.") 