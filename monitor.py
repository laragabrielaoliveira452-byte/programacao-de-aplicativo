temperatura = float(input("Qual a temperatura?: "))
if temperatura < 30:
    print("Clima estavel.")

elif temperatura >= 30:
    print("Alerta de calor!")
    umidade = float(input("Qual a umidade? "))
    if umidade < 40:
        print("Ligar irrigação!")
    else:
        print("Ligue apenas os ventiladores.")