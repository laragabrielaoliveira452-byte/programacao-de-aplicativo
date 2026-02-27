codigo = int(input("Qual o codigo?: "))
nome = input("Qual seu nome?: ")
if nome == "admin" and codigo == 999: 
    print("Acesso liberado. ")
else: 
    print("Acesso negado.")