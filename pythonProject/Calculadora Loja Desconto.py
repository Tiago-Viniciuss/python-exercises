preço = float(input("Qual o preço do produto? "))
print ("""
Formas de Pagamento:
(1) À VISTA:
(2) DÉBITO:
(3) CRÉDITO 2X:
(4) CRÉDITO 3X:""")
formapag = str(input("""

Qual a forma de pagamento? """))
desc1 = preço*10/100
if formapag == "1":
    print (f"O produto custa {round(preço,1)}€, mas você terá um desconto de {round(desc1,1)}€ (10% de desconto) e vai pagar apenas {preço-desc1}€.")
desc2 = preço*5/100
if formapag == "2":
    print (f"O produto custa {round(preço,1)}€, mas você terá um desconto de {round(desc2,1)}€ (5% de desconto) e vai pagar apenas {preço-desc2}€.")
if formapag == "3":
    print (f"O produto custa {round(preço,1)}€.")   
juros = preço*20/100
if formapag == "4":
    print (f"O produto custa {round(preço,1)}€, mas você terá um acréscimo de {juros}€ (20% de juros) e o valor será {preço+juros}€")   
print ("OBRIGADO E VOLTE SEMPRE!")    