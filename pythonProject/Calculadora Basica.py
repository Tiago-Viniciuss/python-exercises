n1 = int(input( "Digite um número: "))
operador = str(input( "Escolha um operador (+,-,x ou ÷): "))
n2 = int(input( "Digite outro número: "))
if operador == "+":
    print (f"{n1}+{n2}={n1+n2}")
if operador == "-":
    print (f"{n1}-{n2}={n1-n2}")
if operador == "x":
    print (f"{n1}x{n2}={n1*n2}")
if operador == "÷":
    print (f"{n1}÷{n2}={n1/n2}")           