codigo = int(input("Qual o codigo?"))
autorizacao = input("Tem autorizaçao?")

if codigo == "999" or autorizacao == "sim":

    bateria = int(input("Coloque o nivel da bateria: "))
    clima = input("Digite o clima: ")
    velocidade = int(input("Coloque a velocidade do vento: "))

    if bateria < 10:
        print("Pouso de emergência autorizado!")
    elif bateria >= 10:
        if clima == "ensolarado" and velocidade <= 30 or clima = chuvoso and velocidade < 10:
            print("POUSO AUTORIZADO: Iniciando descida.")

        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")
                
else:
    print("Drone não identificado, retornando a base.")
       
