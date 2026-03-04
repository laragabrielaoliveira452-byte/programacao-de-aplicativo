salario_inicial = 1000.00
operacao = input("Qual operacao voce ira realizar? ")

if operacao == "depositar":
    depositar = float(input("qual o valor que voce quer depositar? R$: "))
    if depositar > 0.00:
        valor_final = salario_inicial + depositar

elif operacao == "sacar":
    sacar = float(input("qual o valor que deseja sacar? R$: "))
    if (sacar > 0.00 and sacar >= salario_inicial) or sacar == 100.00:
        valor_final = salario_inicial - sacar

elif operacao == "extrato":
    print("seu saldo é: " , salario_inicial)
    valor_final = salario_inicial
    print ("seu saldo agora é " , valor_final)