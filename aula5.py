# Sintaxe de uma lista(array) em python
minhaLista = ["Ana", "Julia", "Eduardo", 10]
print(minhaLista)

# Acesso ao item por posição
print("Acesso por posição: ", minhaLista[2])

# Acesso indexado ao item por posição. -1 é a última posição da lista
print("Acesso indexado negativo: ", minhaLista[-1])

#intervalo de itens
print("Intervalo de itens sem o item de início: ", minhaLista[1:3])
print("Intervalo de itens sem o item de início: ", minhaLista[:3])
print("Intervalo de itens sem o item de final: ", minhaLista[1:])

# Intervalo de indexação negativo
print("Intervalo de itens: ", minhaLista[-3:-1])

# Alterando valor do item
minhaLista[3] = "Christian"
print("Lista com valor do item alterado: ", minhaLista)

# Percorrer lista
for i in minhaLista:
    print("Item da lista: ", i)

# Verificar se o item está na lista
if "Julia" in minhaLista:
    print("Sim,está!")
else:
    print("Não está!")

# Retorna quantidade de itens na lista
print("Quantidade de itens na lista: ", len(minhaLista))

# Adiciona item no final da lista
minhaLista.append("Henrique")
print("Minha lista com novo item no final: ", minhaLista)

# Adiciona item na posição escolhida
minhaLista.insert(1,"Madu")
print("Minha lista com item em posiçao esoecífica: ", minhaLista)

# Remover item específico
minhaLista.remove("Eduardo")
print("MInha lista com item removido: ", minhaLista)

# Remove o índice(se não escoler, removerá o último)
minhaLista.pop(4)
print("Minha lista com índice removido: ", minhaLista)

del minhaLista[1]
print("Minha lista com item removido com o del: ", minhaLista)

# Deleta a lista toda APAGA TUDO
#del minhaLista

# Esvaziar lista
minhaLista.clear()
print("Minha lista vazia com o método clear: ", minhaLista)

minhaLista.insert(0, "hello")
minhaLista.insert(1, "opa")
print("Minha lista com novos itens: ", minhaLista)

# Copia dados de uma lista para outra lista
minhaSegundaLista = minhaLista.copy()
print("Lista que copiou a outra: ", minhaSegundaLista)
minhaTerceiraLista = list(minhaSegundaLista)
print("Lista que copiou a outra: ", minhaTerceiraLista)

# Adiciona itens nas listas
minhaSegundaLista.append("eae")
minhaTerceiraLista.insert(0, "hello")
print("Adicionando novos amiguinhos na segunda lista: ", minhaSegundaLista)
print("Adicionando novos amiguinhos na terceira lista: ", minhaTerceiraLista)

# Contar quantas vezes o item se repete na lista
print("Quantidade de vezes que repete 'hello': ", minhaTerceiraLista.count("hello"))

# Juntando listas
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print("Juntando listas: ", minhaQuartaLista)

# Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ", minhaQuartaLista.index("eae"))