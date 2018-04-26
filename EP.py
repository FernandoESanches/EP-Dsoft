#Considerações: o preço do produto sepre será positivo. 
from firebase import firebase
firebase=firebase.FirebaseApplication('https://ep-design-software.firebaseio.com/', None)
result=firebase.get('EP',None)
loja=input('Nome da loja:')
dicionario=result
acao=int(input(''' 
Controle do estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
Faça sua escolha: '''))
try:
    if loja not in dicionario['lojas']:
        dicionario['lojas'][loja]={'estoque':{},'Lista de produtos em falta':[]}
except TypeError:
    dicionario={'lojas':{loja:{'estoque':{},'Lista de produtos em falta':[]}}}
while acao!=0:
    if acao==1:
        produto=input('Nome do produto: ')
        if produto not in dicionario['lojas'][loja]['estoque']:
            quantidade=int(input('Quantidade inicial:'))
            while quantidade<0:
                print('A quantidade inicial não pode ser negativa.')
                quantidade=int(input('Quantidade inicial:'))               
            preco=float(input('Preço do produto:'))
            while preco<0:
                print('O preço do produto não pode ser negativo')
                preco=float(input('Preço do produto:'))
            dicionario['lojas'][loja]['estoque'][produto]={'quantidade':quantidade, 'preço':preco}
        else:
            print('Produto já cadastrado.')
    elif acao==2:
        produto=input('Nome do produto: ')
        if produto not in dicionario['lojas'][loja]['estoque']:
            print('Elemento não encontrado.')
        else:
            del dicionario['lojas'][loja]['estoque'][produto]
            if produto in dicionario['lojas'][loja]['Lista de produtos em falta']:
                dicionario['lojas'][loja]['Lista de produtos em falta'].remove(produto)
    elif acao==3:
        produto=input('Nome do produto: ')
        if produto not in dicionario['lojas'][loja]['estoque']:
            print('Elemento não encontrado.')
        else:
            quantidade=int(input('Quantidade: '))
            dicionario['lojas'][loja]['estoque'][produto]['quantidade']+=quantidade
            pergunta=input('Alterar preco? 1 para sim e 0 para não.')
            if pergunta=='1':
                preco=float(input('Preço do produto:'))
                while preco<0:
                    print('O preço do produto não pode ser negativo.')
                    preco=float(input('Preço:'))    
                dicionario['lojas'][loja]['estoque'][produto]['preço']=preco
            if dicionario['lojas'][loja]['estoque'][produto]['quantidade'] <= 0:
                dicionario['lojas'][loja]['Lista de produtos em falta'].append(produto)
    elif acao==4:
        soma = 0
        for produto in dicionario['lojas'][loja]['estoque']:
            if dicionario['lojas'][loja]['estoque'][produto]['quantidade']>0:
                print('{0} : {1} unidades'.format(produto, dicionario['lojas'][loja]['estoque'][produto]['quantidade']))  
                soma += dicionario['lojas'][loja]['estoque'][produto]['quantidade'] * dicionario['lojas'][loja]['estoque'][produto]['preço'] 
            else:
                print(('{0} : {1}'.format(produto, 'Produto indisponível')))
        print('O valor total do estoque é: {0} reais'.format(soma))
        if len(dicionario['lojas'][loja]['Lista de produtos em falta']) > 0: 
            print('Os produtos que estão em falta são: {0}'.format(dicionario['lojas'][loja]['Lista de produtos em falta']))
        else:
            print('Não há produtos em falta.')
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
firebase.put('https://ep-design-software.firebaseio.com/','EP',dicionario)
print("Até mais!")
