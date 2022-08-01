print("\t    CALCULADORA \n")
print("Faça sua escolha: \n")
print("(+) - Adição")
print("(-) - Subtração")
print("(*) - Multiplicação")
print("(/) - Divisão")
print("Pressione outra tecla pra sair \n")

operacoes = input("Qual operação deseja fazer?: ") 
if (operacoes  == "+") or (operacoes == "-") or (operacoes == "*") or (operacoes == "/"):

  valor1 = int(input("Digite um valor: ")) # 
  valor2 = int(input("Digite outro valor: "))


if operacoes == "+": 
   resultado = valor1 + valor2
   print(f"O resultado de {valor1} + {valor2} é = {resultado}")
elif operacoes == "-":
   resultado = valor1 - valor2
   print(f"O resultado de {valor1} - {valor2} é = {resultado}")
elif operacoes == "*":
   resultado = valor1 * valor2
   print(f"O resultado de {valor1} * {valor2} é = {resultado}")
elif operacoes == "/":
   resultado = valor1 / valor2
   print(f"O resultado de {valor1} / {valor2} é = {resultado}")
else:
  print("Operação Inválida!")
print("Encerrando Programa...")
