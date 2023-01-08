num1 = int(input("Digite o primeiro número: "))
num2 = int(input ("Digite o segundo número: "))
if num1 == num2:
    print (f"\033[1;31mOs números {num1} e {num2} são iguais.\033[m")
elif num2 == num1:
    print (f"\033[1;31mOs números {num2} e {num1} são iguais.\033[m")    
elif num1 > num2:
    print (f"\033[1;32mO número {num1} é maior que o número {num2}.\033[m")
elif num2 > num1:
    print (f"\033[1;32mO número {num2} é maior que o número {num1}.\033[m")
         