#----------------------------------------------
#          CRIADO POR GABRIEL MELO
#          DATA: 24/Jul/2021
#----------------------------------------------
print("\nCaso queira sair do programa digite(S)")
while True:

    valorProduto = input("Digite o valor do produto: ")
    if valorProduto.lower() == "s":
        break
    adicionar_ou_descontar = input("Deseja adicionar(ADD) ou descontar(DSC)?: ")
    if adicionar_ou_descontar.lower() == "s":
        break
    desconto = input("Digite o valor em %: ")
    if desconto.lower() == "s":
        break
    
    formulaDesconto = (float(desconto) / 100) * float(valorProduto)
    if adicionar_ou_descontar.lower() == "add":
        texto = "adição"
        produtoFinal = float(valorProduto) + formulaDesconto
    elif adicionar_ou_descontar.lower() == "dsc":
        texto = "desconto"
        produtoFinal = float(valorProduto) - formulaDesconto
    else:
        print("Você digitou um valor incorreto|Tente Novamente!|")
    print(f"\nO produto que custava R${valorProduto}") 
    print(f"Com {texto} de '{desconto}%' o produto ficou por R${produtoFinal:.2f}")
