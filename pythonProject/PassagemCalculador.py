distancia= int(input("Quantos KM deu sua viagem? "))
preco = distancia * 0.50
preco2 = distancia * 0.45
if distancia <=200:
    print (f"A distância foi de {distancia}KM e o preço da passagem é {preco}€.")
if distancia >200:
    print (f"A distância foi de {distancia}KM e o preço da passagem é {preco2}€.")    