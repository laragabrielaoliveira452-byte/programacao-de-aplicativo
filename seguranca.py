curso = input ("Você concluiu o curso de programaçao?")

if curso == " sim ":
    instrutor = input ("O instrutor está na sala?")
    if instrutor == "sim":
        print ("Acesso Liberado: Operação iniciada")
    else:
        print ("Aguarde o instrutor para ligar a maquina")

else:
    print ("Acesso Negado: Faça o treinamento primeiro")