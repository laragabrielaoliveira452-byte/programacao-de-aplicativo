nota = float(input("Coloque a sua nota: "))
presença = int(input("Coloque sua presença: "))

if nota >= 70 and presença >= 75:
    print("Você foi aprovado!")

elif nota <= 70 and presença <= 75:
    print("Você foi reprovado. Verifique sua nota ou presença")

elif nota <= 70 and presença >= 75:
    print("você foi reprovado.")

elif nota >= 70 and presença <= 75:
    print("você foi reprovado")
