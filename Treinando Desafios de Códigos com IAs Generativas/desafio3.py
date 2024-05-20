import sys

# Definindo a lista de dicionários com os modelos disponíveis
modelos_disponiveis = [
    {"nome": "Claude 3 Opus", "pontuacao_desempenho": 9, "preco_mensal": 600},
    {"nome": "Claude 3 Sonnet", "pontuacao_desempenho": 8, "preco_mensal": 450},
    {"nome": "Claude 3 Haiku", "pontuacao_desempenho": 7, "preco_mensal": 350}
]

def recomendar_modelo(modelos, orcamento):
    if orcamento < 250:
        return ("None", "Seu orçamento é muito baixo para recomendar um modelo adequado.")
    
    # Filtrando modelos que estão dentro do orçamento
    modelos_adequados = [modelo for modelo in modelos if modelo["preco_mensal"] <= orcamento]
    
    if not modelos_adequados:
        # Se nenhum modelo está dentro do orçamento, retorna o mais próximo
        modelo_mais_proximo = min(modelos, key=lambda x: abs(x["preco_mensal"] - orcamento))
        return (modelo_mais_proximo["nome"], f"{modelo_mais_proximo['nome']}. Este modelo está mais próximo do seu orçamento.")
    
    # Selecionando o modelo com a melhor pontuação de desempenho dentre os que estão dentro do orçamento
    modelo_recomendado = max(modelos_adequados, key=lambda x: x["pontuacao_desempenho"])
    
    return (modelo_recomendado["nome"], f"{modelo_recomendado['nome']}. Melhor desempenho dentro do seu orçamento.")

# Leitura da entrada do usuário
orcamento = int(sys.stdin.readline().strip())

# Fazendo a recomendação do modelo
modelo, mensagem = recomendar_modelo(modelos_disponiveis, orcamento)

# Saída da recomendação
print(mensagem)

