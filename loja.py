valor_total = float(input("Digite o valor total: "))
cupom = (input("Digite o nome do cupom: "))

desconto = valor_total * 0.10
novo_preço = valor_total - desconto

if cupom == "DEV10":
    print("cupom valido " , novo_preço)

else:
    print("cupons invalido", valor_total)
