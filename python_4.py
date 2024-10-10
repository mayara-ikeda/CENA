# LISTA DE EXERCÍCIOS PYTHON 4
# FEITO POR: MAYARA PARDI IKEDA

# 1) Para as próximas tarefas sobre listas, utilize o interpretador:

## A) Crie uma lista com 5 coisas que você gosta.
coisas_que_gosto = ['café','feijoada','açaí','sashimi','okonomiyaki']

## B) Utilize a função print() para imprimir sua lista.
print(coisas_que_gosto)

## C) Utilize a função print() para imprimir o elemento do meio.
print(coisas_que_gosto[2])

## D) Agora, substitua o elemento do meio por outro item, como sua música favorita ou um pássaro cantor.
coisas_que_gosto[2] = "Carpenters"

## E) Utilize a mesma instrução de impressão de b. para imprimir sua nova lista.
print(coisas_que_gosto)

## F) Adicione um novo elemento no final.
coisas_que_gosto.append("coca-cola")
print(coisas_que_gosto)

## G) Adicione um novo elemento no começo.
coisas_que_gosto.insert(0,"coxinha")
print(coisas_que_gosto)

## H) Adicione um novo elemento em algum lugar que não seja no início ou no final.
coisas_que_gosto.insert(1,"brigadeiro")
print(coisas_que_gosto)

## I) Remova um elemento do final.
coisas_que_gosto.pop()
print(coisas_que_gosto)

## J) Remova um elemento do começo.
coisas_que_gosto.pop(0)
print(coisas_que_gosto)

## K) Remova um elemento de algum lugar que não seja no início ou no final.
coisas_que_gosto.pop(2)
print(coisas_que_gosto)

## L) Use join para criar uma string. Junte os elementos com ', '.
resultado_do_join = ', '.join(coisas_que_gosto)
print(resultado_do_join)

#-------------------------------------------------------------------------------------------#

# 2) Escreva um script que divida uma string em uma lista. No seu script:

## A) Salve a string sapiens, erectus, neanderthalensis como uma variável chamada taxa.
taxa = "sapiens, erectus, neanderthalensis"

## B) Print taxa.
print(taxa)

## C) Print taxa[1], o que você obtém?
print(taxa[1]) # Obtive a letra "a" como resultado

## D) Print type(taxa). Qual é o tipo?
print(type(taxa)) # é do tipo string: <class 'str'>

## E) Divida taxa em palavras individuais e print o resultado da divisão. (Pense em ', '.)
resultado_do_split = taxa.split(', ')

## F) Armazene o resultado do split em uma nova variável chamada species.
species = resultado_do_split

## G) Print species.
print(species)

## H) Print the species[1], o que você obtém?
print(species[1]) # Obtive 'erectus' como resultado

## I) Print type(species). Qual é o tipo?
print(type(species)) # é do tipo lista: <class 'list'>

## J) Ordene a lista em ordem alfabética e print (dica: pesquise a função sorted()).
ordem_alfabetica = sorted(species, key=None, reverse= False)
print(ordem_alfabetica)

## K) Ordene a lista pelo comprimento de cada string e print. (A string mais curta deve vir primeiro).
ordem_de_comprimento = sorted(species, key=len, reverse= False)
print(ordem_de_comprimento)

#-------------------------------------------------------------------------------------------#

# 3) Usando o interpretador Python, investigue a diferença entre essas duas maneiras de copiar uma lista. Cuidado! Uma delas pode NÃO ser o que você espera.

# Método 1:
# Crie uma lista. Exemplo: my_list = ['a', 'bb', 'ccc']
my_list = ['a','b','c','d','e']

# Faça uma cópia usando o operador de atribuição =: list_copy = my_list
list_copy = my_list

# Print a lista original print(my_list)
print(my_list)

# Altere a list_copy adicionando um novo elemento usando append()
list_copy.append("f")
print(list_copy)

# print a lista original novamente print(my_list)
print(my_list)

# Método 2:
# Crie uma lista. Exemplo: my_list2 = ['a', 'bb', 'ccc']
my_list2 = ['aa','bb','cc','dd','ee']

# Faça uma cópia com o método copy(): list_copy2 = my_list2.copy()
list_copy2 = my_list2.copy()

# Print a lista original print(my_list2)
print(my_list2)

# Altere a list_copy2 adicionando um novo elemento usando append()
list_copy2.append("ff")
print(list_copy2)

# print a lista original novamente print(my_list2)
print(my_list2)

#-------------------------------------------------------------------------------------------#

# 4) Escreva um script que use um loop while para imprimir os números de 1 a 100.
i=0
while i<100:
    i=i+1   
    print(i)

#-------------------------------------------------------------------------------------------#

# 5) Escreva um script que use um loop while para calcular o fatorial de 1000.
numero = 1000
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
print(f"O fatorial de {numero} é {fatorial}")

#-------------------------------------------------------------------------------------------#

# 6) Itere por cada elemento desta lista usando um loop for: [101,2,15,22,95,33,2,27,72,15,52]. Print apenas os valores que são pares (dica: use o operador módulo).
lista = [101,2,15,22,95,33,2,27,72,15,52]
for i in lista:
    if i%2==0:
     print(i)

#-------------------------------------------------------------------------------------------#

# 7) Ordene os elementos da lista acima e, em seguida, itere por cada elemento usando um loop for e:
# Print cada elemento.
lista_ordenada = sorted(lista,key=None)
for item in lista_ordenada:
   print(item)

#Calcule duas somas acumulativas, uma de todos os valores pares e outra de todos os valores ímpares.
#Print apenas as duas somas finais. A saída do seu script deve ser:
    # Soma dos números pares: 150 
    # Soma dos números ímpares: 286
soma_pares=0
for item in lista_ordenada:
   if item%2==0:
      soma_pares=soma_pares+item
print(f"Soma dos números pares: {soma_pares}")

soma_impares=0
for item in lista_ordenada:
   if item%2!=0:
      soma_impares=soma_impares+item
print(f"Soma dos números ímpares: {soma_impares}")

#-------------------------------------------------------------------------------------------#

# 8) Escreva um script que use range() em um loop for para imprimir todos os números de 0 a 99.
for i in range(100):
    print(i)
# Modifique seu loop para imprimir todos os números de 1 a 100.
for i in range(1,101):
    print(i)

#-------------------------------------------------------------------------------------------#

# 9) Crie um novo script que use a compreensão de lista para fazer o mesmo que o problema 8. (Use range() para imprimir todos os números de 1 a 100.)
numeros = [i for i in range(1, 101)]
print(numeros)

#-------------------------------------------------------------------------------------------#

# 10) Escreva um novo script que receba os valores de início e fim pela linha de comando. Se você chamar seu script assim count.py 3 10, ele imprimirá os números de 3 a 10.
# Modifique seu script para imprimir apenas o número se ele for ímpar.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: ")) + 1 # esse +1 garante que a lista não pare no número anterior

lista2 =[i for i in range(valor1,valor2)]

print(lista2)

#-------------------------------------------------------------------------------------------#

# 11) Escreva um novo script para criar uma lista com os seguintes dados ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use um loop for para iterar por cada elemento desta lista e:
# Print cada elemento.
lista3 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in lista3:
    print(i)
# Print o comprimento e a sequência, separados por uma guia. A saída deve se parecer com:
# 14	ATGCCCGGCCCGGC
# 25	GCGTGCTAGCAATACGATAAACCGG
# 12	ATATATATCGAT
# 8 	ATGGGCCC
for i in lista3:
    print(f"{len(i)}\t{i}")

# 12) Use a compreensão de lista para gerar uma lista de tuplas. As tuplas devem conter sequências e comprimentos do problema anterior. Print o comprimento e a sequência (ou seja, "4\tATGC\n"). Uma lista de tuplas se parece com isso [(4,'ATGC'),(2,'GC')].

lista_tuplas = [(len(seq), seq) for seq in lista3]
print(lista_tuplas)

for comprimento, seq in lista_tuplas:
    print(f"{comprimento}\t{seq}")
#-------------------------------------------------------------------------------------------#

# 13) Modifique o script do #11 para que você também imprima o número (posição na lista) de cada sequência (ou seja, "1\t4\tACGT\n").
for i, seq in enumerate(lista3, start=1):
    print(f"{i}\t{len(seq)}\t{seq}")

#-------------------------------------------------------------------------------------------#

# 14) Você tem commitado seu trabalho?
#Siiim

