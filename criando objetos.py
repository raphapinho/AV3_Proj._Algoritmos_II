valores = [1, 2, 3, 4, 5]  # Lista de valores

for i, valor in enumerate(valores):
    nome_variavel = f"variavel_{i}"  # Nome da variável usando o índice do loop
    exec(f"{nome_variavel} = {valor}")  # Criação da variável dinamicamente usando 'exec'
    print(f"{nome_variavel} = {valor}")  # Exibe o nome da variável e seu valor

