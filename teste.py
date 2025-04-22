import matplotlib.pyplot as plt

# Exemplo de dicionário
dados = {'Maçã': 10, 'Banana': 15, 'Laranja': 7, 'Uva': 12}

# Separando as chaves e os valores
categorias = list(dados.keys())
valores = list(dados.values())

# Criando o gráfico de barras
plt.bar(categorias, valores, color='skyblue')

# Adicionando título e rótulos
plt.title('Quantidade de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Quantidade')

# Exibindo o gráfico
plt.show()
