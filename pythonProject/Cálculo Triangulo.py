p1 = float(input ("Digite um número: "))
p2 = float(input ("Digite outro número: "))
p3 = float(input ("Digite o último número: "))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print ("Os segmentos formam um triângulo!") 
else:
    print ("Os segmentos não formam um triângulo!")
