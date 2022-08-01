
#-----------------------Inicio da Função volumeFeijoada-------------------------


def volumeFeijoada(): # Primeira função
  while True: # Loop
      try: #Feito um try/except para caso se digitar um valor não numérico
        print('#Menu volume feijoada#')
        volume = float(input('Digite a quantidade que deseja (em ml ): ')) # Pergunta a quantidade de de feijoada em ml
        if 300<= volume <= 5000:
          return 0.08 * volume # Retorna o valor em R$
        elif volume < 300: # Retorna um print caso digite um valor menor que 300ml
          print('Não aceitamos porções menores que 300ml. Por favor, tente novamente!')
        elif volume > 5000: # Retorna um print caso digite um valor menor que 5l
          print('Não aceitamos porções maiores que 5l. Por favor, tente novamente!')
        else:
          print('Opção inválida. Por favor, tente novamente!')
      except ValueError: # Tratamento de erro (valor não numérico)
          print('Você digitou um valor não numérico. Por favor, tente novamente!')
          continue


#-------------------------Fim da Função volumeFeijoada--------------------------
#-------------------------Inicio da Função opcaoFeijoada------------------------


def opcaoFeijoada(): # Segunda função
  while True : # Loop
    print('\n#Menu Opção feijoada#')
    opcao = input('Entre com a opção de feijoada desejada:\n'
                  'b - Básica (Feijão + paiol + costelinha).\n'
                  'p - Premíum (Feijão + paiol + costelinha + partes do porco).\n'
                  's - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon).\n'
                  '\n>> ') # Pergunta a opção desejada 
    if opcao == 'b': # Retorno da opção conforme a escolha
      return 1.00 # Multiplicador
    elif opcao == 'p':
      return 1.25
    elif opcao == 's':
      return 1.50
    else: # Um else caso digite uma opção inválida
      print('Opção inválida!') 
      continue


#------------------------Fim da Função opcaoFeijoada----------------------------
#------------------------Inicio da Função acompanhamentoFeijoada----------------


def acompanhamentoFeijoada(): # Terceira função
  final = 0 # Contador
  while True: # Loop
    print('\n#Menu acompanhamento feijoada#')
    acompanhamento = int(input('Deseja acompanhamento?\n'
                            '0- Não desejo mais acompanhamento (encerrar pedido).\n'
                            '1 - 200g de arroz.\n'
                            '2 - 150g de farofa especial.\n'
                            '3 - 100g de couve cozida.\n'
                            '4 - 1 laranja descascada.\n'
                            '\n >> ')) # Pergunta se quer acompanhamento
    if acompanhamento == 0:
      return final # Caso a escolha for 0, o programa Encerra
    elif acompanhamento == 1:
       final = final + 5.00 # Soma + multiplicador
    elif acompanhamento == 2:
       final = final + 6.00
    elif acompanhamento == 3:
       final = final + 7.00
    elif acompanhamento == 4:
       final = final + 3.00
    else: # Um else caso digite uma opção inválida
      print('Opção inválida, Por favor tente novamente!')
      continue
    

# -----------------------Fim da Função acompanhamentoFeijoada-------------------
#------------------------Inicio da Main-----------------------------------------


print('#Bem-vindo ao Programa de Feijoada do Kelvin Silva Ferreira#\n') # Início com Identificador Pessoal
print('===========/=============/============/============/==============')

# Variáveis das funções
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
final = (volume * opcao) + acompanhamento # Equação do valor

print(f'\nO valor total a pagar é RS: {final} (volume = {volume} * opção = {opcao} + adicionais = {acompanhamento})') # Soma do valor total a ser pago6
print('===========/=============/============/============/==============')


#-----------------------Fim da MAIN---------------------------------------------
