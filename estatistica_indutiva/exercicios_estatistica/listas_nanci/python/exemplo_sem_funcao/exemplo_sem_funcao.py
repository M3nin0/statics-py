'''
Exemplo de como såo feitos a média, mediana e desvio padråo
'''

# Média aritmética simples
# Todos os valores tem o mesmo peso

# Ex: Um time de futebol marcou 3, 1, 5 e 2 gols nos quatros jogos
# iniciais do campeonato. Calcule a média de gols por jogo da
# equipe nessas primeiras 4 partidas

gols = [3, 1, 5, 2]

'''
Media = x / n, onde x é a soma do rol e o n é a quantidade de elementos
'''
media = sum(gols) / len(gols)
print("Exemplo 1 - média aritmética simples " + str(media))

## Veja que todos os gols tem a mesma importancia

## Média aritmética ponderada

## Ex: Calcule a nota média de uma prova, realizada por 12 alunos
## cujas notas såo apresentadas a seguir:

## n˚ de alunos X Notas
## 4     x    10
## 2     x    8.5
## 3     x    6.0
## 3     x    5.0

valores = [10, 8.5, 6.0, 5.0]
peso = [4, 2, 3, 3]

'''
A média aritmética ponderada leva em consideraçåo o peso dos valores
Para realiza-la é necessário entåo:

    elemento * peso / soma dos pesos
'''

total = 0
for i in range(0, len(valores)):
    total += valores[i] * peso[i]

print('Exemplo 2: ' + str(total / sum(peso)))


# Mediana

## Mediana: Valor que ocupa a posiçåo central do rol

## Para realizar calculos de mediana é necessário ter um rol
## Rol: Organizaçåo dos dados em ordem crescente ou descrescente

'''
Posiçao da mediana:
    n + 1 / 2
Onde n é a quantidade de valores do Rol
'''

## Exe: Encontre a mediana e a nota modal da tabela a seguir

# N˚ de alunos   X  notas
# 4     x   7.0
# 2     x   5.0
# 2     x   6.0
# 1     x   9.5

rol = [5, 5, 6, 6, 7, 7, 7, 7, 9.5]

mediana = int((len(rol) / 2 ) / + 1)

print('Exemplo 3: ' + str(int(rol[mediana])))

# Caso haja algum valor de mediana par, basta pegar as partes do meio envolvidas e
# e tirar a média simples

# Moda

## Amodal: Nåo tem moda
## Unimodal: Tem apenas uma moda
## Bimodal: Possui duas modas

## Para encontrar a moda basta verificar o valor que mais aparece no rol

## No caso do exemplo acima, é o 7

# Desvio padrão
