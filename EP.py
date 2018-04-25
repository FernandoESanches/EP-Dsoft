#Considerações: o preço do produto sepre será positivo. 
import json
loja=input('Nome da loja:')
try:
    with open('lojas.txt', 'r') as arquivo2:
        b=arquivo2.read()
        lojas=json.loads(b)
except FileNotFoundError:
    lojas=[]
    lojas.append(loja)
if loja not in lojas:
    lojas.append(loja)
try:    
    with  open('estoque_{0}.txt'.format(loja), 'r') as arquivo:
        a=arquivo.read()
        estoque=json.loads(a)
except FileNotFoundError:
    estoque=dict()
try:
    with open('listaneg_{0}.txt'.format(loja), 'r') as novo_arquivo:
        c=novo_arquivo.read()
        lista_de_produtos_negativos=json.loads(c)
except FileNotFoundError:
    lista_de_produtos_negativos=[]
acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))

while acao!=0:
    if acao==1:
        produto=input('Nome do produto: ')
        if produto not in estoque:
            quantidade=int(input('Quantidade inicial:'))
            while quantidade<0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade=int(input('Quantidade inicial:'))               
            preco=float(input('Preço do produto (em reais):'))
            while preco<0:
                print('O preço do produto não pode ser negativo')
                preco=float(input('Preço do produto (em reais):'))
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
                preco=float(input('Preço do produto (em reais):'))
                while preco<0:
                    print('O preço do produto não pode ser negativo.')
                    preco=float(input('Preço do produto (em reais):'))    
                estoque[produto]['preço']=preco
            if estoque[produto]['quantidade'] < 0:
                lista_de_produtos_negativos.append(produto)
    elif acao==4:
        soma = 0
        for produto in estoque:
            print('{0} : {1}'.format(produto, estoque[produto]['quantidade']))  
            if estoque[produto]['quantidade'] >0:
                soma += estoque[produto]['quantidade'] * estoque[produto]['preço']  
        print('O valor total do estoque é: {0}'.format(soma))
        if len(lista_de_produtos_negativos) > 0: 
            print('Os produtos de quantidade negativa são: {0}'.format(lista_de_produtos_negativos))
        else:
            print('Não há produtos de quantidade negativa.')
    else:
        print('Comando inválido.')
    acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
dicionario=json.dumps(estoque, sort_keys=True, indent=4)
lista=json.dumps(lojas, sort_keys=True, indent=4)
listaneg=json.dumps(lista_de_produtos_negativos, sort_keys=True, indent=4)
with open('estoque_{0}.txt'.format(loja), 'w') as arquivo:
    arquivo.write(dicionario)
with open('lojas.txt', 'w') as arquivo4:
    arquivo4.write(lista)
with open('listaneg_{0}.txt'.format(loja), 'w') as arquivo_novo:
    h=arquivo_novo.write(listaneg)
print("Até mais!")