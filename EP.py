acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
estoque=dict()
while acao!=0:
    if acao==1:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            quantidade=int(input('Quantidade inicial: '))
            while quantidade<0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade=int(input('Quantidade inicial: '))
            estoque[produto]={'quantidade':quantidade}
        else:
            print('Produto já cadastrado.')
    elif acao==2:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            print('Elemento não encontrado.')
        else:
            del estoque[produto]
    acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
