# Como mostrar algo na tela para o usuário.
print("alo")
print('alo')
# Declaração de variável e tipo de dados.
numeroInteiro = 2
numeroDecimal = 2.12362351
nome = "Christian"
sobrenome = 'Giuliani'
verdadeiroFalso = True
# Mostrando na tela os valores armaenados nas variáveis.
print(numeroInteiro)
print(numeroDecimal)
print(nome)
print(sobrenome)
print(verdadeiroFalso)
# Mostrando na tela o tipo de dado que a variável armazena.
print(type(numeroInteiro))
print(type(numeroDecimal))
print(type(nome))
print(type(sobrenome))
print(type(verdadeiroFalso))
# Recursos para usar com dados do tipo String
# Função 'len' conta a quantidade de caracter
print(len(nome))
# Para repetir valor da variável, usar * e colocar a quantidade de vezes que será repetido
print(nome  * 3)
# Concatenando Strings
print(nome + '', sobrenome)
print(nome + ' Giuliani')
# Recursos para usar com dados do tipo float
print(numeroDecimal)
# Arredondar e definir quantas casas decimais
print(round(numeroDecimal,3))
print("%.3f" % (numeroDecimal)) 