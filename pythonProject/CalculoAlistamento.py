resposta = int(input("Qual a sua idade atual? "))
idademax = 18
if resposta < idademax:
    print (f"Ainda não é hora de se alistar, mas você terá que fazer isso daqui a {idademax-resposta} anos . ")
elif resposta > idademax:
    print (f"Recruta, prazo para se alistar já passou. Você está atrasado {resposta-idademax} anos.")
else:
    print ("Muito bem, recruta! É hora de se alistar!")        