valor = float(input("Qual o valor da casa? R$ " ))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos pretende pagar? "))
meses = anos * 12
valorparcela = valor / meses 
if valorparcela > salario*30/100:
    print (f"\033[1;31mInfelizmente, para comprar uma casa de R${valor:.2f} e pagar em {anos} anos, seria necessário uma parcela de R${valorparcela:.2f} por mês\033[m.")
else:
    print ("\033[1;32mParabéns, o seu empréstimo foi aprovado!\033[m")    