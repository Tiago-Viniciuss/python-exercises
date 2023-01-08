nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media <= 5.0:
    print (f"A sua média foi {media} pontos, portanto você foi \033[1;31mREPROVADO!\033[m")
elif media > 5.0 and media < 7.0:
    print (f"A sua média foi {media} pontos, portanto você está de \033[1;33mRECUPERAÇÃO!\033[m")
elif media >= 7.0:
    print (f"A sua média foi {media} pontos, portanto você foi \033[1;32mAPROVADO!\033[m")        