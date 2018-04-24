#Considerações: o preço do produto sepre será positivo. 
import json
lojas=[]
loja=input('Nome da loja')
acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
try:    
    with  open('estoque.txt', 'r') as arquivo:
        a=arquivo.read()
        estoque=json.loads(a)
except FileNotFoundError:
    estoque=dict()
lista_de_produtos_negativos = []
while acao!=0:
    if acao==1:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            quantidade=int(input('Quantidade inicial:'))
            while quantidade<0:
                print('A quantidade inicial não pode ser negativa')
                quantidade=int(input('Quantidade inicial:'))
            estoque[produto]={'quantidade':quantidade}                
            preco=float(input('Preço do produto:'))
            while preco<0:
                print('O preço do produto não pode ser negativo')
                preco=float(input('Preço do produto:'))
            estoque[produto]={'quantidade':quantidade, 'preço':preco}
        else:
            print('Produto já cadastrado.')
    elif acao==2:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            print('Elemento não encontrado.')
        else:
            del estoque[produto]
    elif acao==3:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            print('Elemento não encontrado.')
        else:
            quantidade=int(input('Quantidade: '))
            estoque[produto]['quantidade']+=quantidade
            pergunta=input('Alterar preco? 1 para sim e 0 para não.')
            if pergunta=='1':
                preco=float(input('Preço do produto:'))
                while preco<0:
                    print('O preço do produto não pode ser negativo.')
                    preco=float(input('Preço:'))    
                estoque[produto]['preço']=preco
            if estoque[produto]['quantidade'] < 0:
                lista_de_produtos_negativos.append(produto)
    elif acao==4:
        soma = 0
        for produto in estoque:
            print('{0} : {1}'.format(produto, estoque[produto]['quantidade']))  
        if estoque[produto]['quantidade'] >0:
            for i in estoque[produto]:
                soma += estoque[produto]['quantidade'] * estoque[produto]['preço']  
        print('O valor total do estoque é: {0}'.format(soma))
        if len(lista_de_produtos_negativos) > 0: 
            print('Os produtos de quantidade negativa são: {0}'.format(lista_de_produtos_negativos))
        else:
            print('Não há produtos de quantidade negativa')
    acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
dicionario=json.dumps(estoque, sort_keys=True, indent=4)
with open('estoque.txt', 'w') as arquivo:
    arquivo.write(dicionario)
print("Até mais!")