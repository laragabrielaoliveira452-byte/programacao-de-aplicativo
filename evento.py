idade = int(input("Qual a sua idade? "))
saldo = float(input("Qual o seu saldo? "))

if idade >= 18 and saldo >= 50:
    print("Acesso liberado! Bem-vindo ao evento.")

elif idade <= 18 and saldo <= 50: 
    print("Acesso negado.")

elif idade <= 18 and saldo >= 50:
    print("Acesso negado.")
elif idade >= 10 and saldo<= 50:
    print("Acesso negado.")