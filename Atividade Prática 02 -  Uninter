final = 0 # O contador deve iniciar em zero.

print(' #Bem vindos a pizzaria do Kelvin Silva Ferreira#\n') # Identificador pessoal.
print('---------------------Cardápio-----------------------') # Cardápio.
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('|   21   | Napolitana |    R$ 20,00 |    R$ 26,00  |')
print('|   22   | Margherita |    R$ 20,00 |    R$ 26,00  |')
print('|   23   | Calabresa  |    R$ 25,00 |    R$ 32,00  |')
print('|   24   | Toscana    |    R$ 30,00 |    R$ 39,00  |')
print('|   25   | Portuguesa |    R$ 30,00 |    R$ 39,00  |')
print('----------------------------------------------------')

while True: # Loop

  tamanho = input('Qual o tamanho da pizza que deseja? (M/G): ') # Input pedindo tamanho desejado da pizza.
  
  # if com os tamanhos e else caso digite alguma opção inválida. 
  if tamanho == 'M' : 
     multiplicador = 1
  elif tamanho == 'G'  :
     multiplicador = 1.30
  else:
     print('Opção inválida')
     continue

  codigo = input('Entre com o código do sabor: ') # Input pedindo código da pizza.

  # if com os códigos das pizzas com print identificando o sabor e else caso digite uma opção inválida.
  if codigo == '21':
     final = final + 20 * multiplicador
     print('Você pediu uma pizza sabor Napolitana.')
  elif codigo == '21':
       final = final + 26 * multiplicador
       print('Você pediu uma pizza sabor Napolitana.')
  elif codigo == '22':
       final = final + 20 * multiplicador
       print('Você pediu uma pizza sabor Margherita.')
  elif codigo == '22':
       final = final + 26 * multiplicador
       print('Você pediu uma pizza sabor Margherita.')
  elif codigo == '23':
       final = final + 25 * multiplicador
       print('Você pediu uma pizza sabor Calabresa.')
  elif codigo == '23':
       final = final + 32.50 * multiplicador
       print('Você pediu uma pizza sabor Calabresa.')
  elif codigo == '24':
       final = final + 30 * multiplicador
       print('Você pediu uma pizza sabor Toscana.')
  elif codigo == '24':
       final = final + 39 * multiplicador
       print('Você pediu uma pizza sabor Toscana.')
  elif codigo == '25':
       final = final + 30 * multiplicador
       print('Você pediu uma pizza sabor Portuguesa.')
  elif codigo == '25':
       final = final + 39 * multiplicador
       print('Você pediu uma pizza sabor Portuguesa.')
  else:
     print('Opção inválida !')
     continue

  resposta = input('Deseja continuar o pedido? (S/N): ') # Input perguntando se deseja continuar a pedir.

  # if se caso a resposta for sim, continuar a pedir e else caso a resposta for não, encerrar pedido com um valor final.
  if resposta == 'S':
     continue
  else:
     print(f'O valor final do seu pedido é: R$ {final}')
     break
