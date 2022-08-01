listaProdutos = [] # Lista Global

#------------------Início da função cadastrarProdutos-------------------


def cadastrarProdutos(codigo): # Primeira função com um parâmetro
  print('Bem vindos ao CADASTRAR PRODUTOS')
  print(f'O código do produto a ser cadastrato é: {codigo}')
  produto = input('Digite o nome do produto: ') # Input pedindo para informar o nome do produto
  fabricante = input('Digite o nome do fabricante do produto: ') # Input pedindo para informar o nome do fabricante
  valor = float(input('Digite o valor do produto, por favor!: R$ ')) # Input pedindo para informar o valor do produto
  dicionarioProduto = {'codigo' : codigo, 
                       'produto' : produto,
                       'fabricante' : fabricante,
                       'valor' : valor} # Dicionário criado
  listaProdutos.append(dicionarioProduto.copy()) # Copiando dicionário para lista

#------------------Fim da função cadastrarProdutos----------------------
#------------------Início da função consultarProdutos-------------------


def consultarProdutos(): # Segunda função
  print('Bem vindos ao CONSULTAR PRODUTOS') # Segunda Função
  while True: # Feito um try/except para caso se digitar um valor não numérico
    try:
      opConsultar = int(input('Digite a opção desejada:\n'
                          '1-Consultar todos os produtos\n'
                          '2-Consultar Produtos por Código\n'
                          '3-Consultar Produtos por Fabricante\n'
                          '4-Retornar'
                          '\n>> '))
      if opConsultar == 1:
        print('Bem vindos ao CONSULTAR TODOS OS PRODUTOS')
        for produto in listaProdutos: # selecionar cada dicionário da minha lista
          for key, value in produto.items(): # Procurando chaves e valores dentro de itens
            print(f'{key} : {value}')
      elif opConsultar == 2:
        print('Bem vindos ao CONSULTAR PRODUTOS POR CÓDIGOS')
        entrada = int(input('Digite o código desejado: '))
        for produto in listaProdutos: # selecionar cada dicionário da minha lista
          if (produto['codigo'] == entrada):
            for key, value in produto.items(): # Procurando chaves e valores dentro de itens
                print(f'{key} : {value}')
      elif opConsultar == 3:
        print('Bem vindos ao CONSULTAR PRODUTOS POR FABRICANTES')
        entrada = input('Digite o fabricante: ')
        for produto in listaProdutos: # selecionar cada dicionário da minha lista
          if (produto['fabricante'] == entrada):
            for key, value in produto.items(): # Procurando chaves e valores dentro de itens
              print(f'{key} : {value}')
      elif opConsultar == 4:
        print('Retornando ao menu...')
        return
      else: # Um else caso digite uma opção inválida
        print('Opção Inválida')
        continue
    except ValueError: # Tratamento de erro (valor não numérico)
        print('Você digitou uma valor não inteiro, por favor tente novamente!' )
        continue


#------------------Fim da função consultarProdutos---------------------
#------------------Início da função removerProdutos--------------------


def removerProdutos(): # Terceira função
  print('Bem vindos ao REMOVER PRODUTOS')
  entrada = int(input('Digite o código a ser removido: '))
  for produto in listaProdutos: # selecionar cada dicionário da minha lista
    if (produto['codigo'] == entrada):
      listaProdutos.remove(produto) # Removendo produto um produto dentro da lista


#------------------Fim da função removerProdutos-----------------------
#------------------Início da MAIN--------------------------------------

registroProdutos = 0 # Contador deve sempre iniciar com 0

print('Bem vindos ao controle de Estoque do Kelvin Silva Ferreira') # Início com Identificador Pessoal
while True:
  try:
    opcao = int(input('Digite a opção desejada:\n'
                        '1-Cadastrar Produto\n'
                        '2-Consultar Produto\n'
                        '3-Remover Produto\n'
                        '4-Sair'
                        '\n>> '))
    if opcao == 1:
      registroProdutos = registroProdutos + 1 # Contador + opcao
      cadastrarProdutos(registroProdutos)
    elif opcao == 2:
      consultarProdutos()
    elif opcao == 3:
      removerProdutos()
    elif opcao == 4:
      print('Saindo do programa...') 
      break
    else: # Um else caso digite uma opção inválida
      print('Opção Inválida')
      continue
  except ValueError: # Tratamento de erro (valor não numérico)
      print('Você digitou uma valor não Inteiro, por favor tente novamente!' )


#------------------Fim da MAIN-----------------------------------------
