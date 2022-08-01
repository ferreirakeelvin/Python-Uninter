print("\t\t Loja Pythonica \n")# Nome da loja
print("Olá, essa é a loja do Kelvin Silva Ferreira, sejam bem vindos! \n")# Saudação da loja com meu identificador pessoal.
print("-----------//--------------//-------------//-------------------")

valor_produto = float(input("Digite o valor do produto (Colocar um '.' no lugar da ','): "))# Solicitação do valor do produto.
quantidade_produto = int(input("Digite a quantidade: "))# Solicitação da quantidade de produtos.

# Não há desconto se a quantidade solicitada for menor que 5 unidades.
if quantidade_produto <= 4:
  resultado = valor_produto * quantidade_produto
  print(f"Você não recebeu desconto, logo o valor total do produto foi de: R${resultado}")

# Desconto de 3% para solicitação de produtos entre 5 e 19 unidades.
elif quantidade_produto >= 5 and quantidade_produto <= 19:
  resultado = valor_produto * quantidade_produto
  print(f"O valor sem desconto foi de: R${resultado}")
  desconto = resultado * 3/100
  valor_total = resultado - desconto
  print(f"O valor com desconto foi de: R${valor_total} (3% de desconto)")

# Desconto de 6% para solicitação de produtos entre 20 e 99 unidades.
elif quantidade_produto >= 20 and quantidade_produto <= 99:
  resultado = valor_produto * quantidade_produto
  print(f"O valor sem desconto foi de: R${resultado}")
  desconto = resultado * 6/100
  valor_total = resultado - desconto
  print(f"O valor com desconto foi de: R${valor_total} (6% de desconto)")

# Desconto de 10% para solicitação de produtos maior ou igual a 100 unidades .
else:
  quantidade_produto >= 100
  resultado = valor_produto * quantidade_produto
  print(f"O valor sem desconto foi de: R${resultado}")
  desconto = resultado * 10/100
  valor_total = resultado - desconto
  print(f"O valor com desconto foi de: R${valor_total} (10% de desconto)")

print("-----------//--------------//-------------//-------------------\n")
print("Obrigado e volte sempre!")
