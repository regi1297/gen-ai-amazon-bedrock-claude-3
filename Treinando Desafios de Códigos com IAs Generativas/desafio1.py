import sys

# Definindo as características dos modelos Claude 3
modelos_claude_3 = {
    "Automatizar tarefas, criar aplicações voltadas para o usuário que geram receita e acelerar a pesquisa e o desenvolvimento em diversos setores.": "Claude 3 Opus",
    "Equilíbrio ideal entre inteligência e velocidade, especialmente para workloads corporativas. Ele se destaca em raciocínio complexo, criação de conteúdo diferenciado, consultas científicas, matemática e codificação.": "Claude 3 Sonnet",
    "Resposta rápida e capacidade de resposta quase instantânea, imitação das interações humanas, moderar conteúdo, otimizar gerenciamento de inventário, produzir traduções rápidas e precisas, resumir dados não estruturados.": "Claude 3 Haiku"
}

# Lendo a entrada do usuário
descricao = sys.stdin.readline().strip()

# Verificando a descrição e retornando o modelo correspondente
if descricao in modelos_claude_3:
    print(modelos_claude_3[descricao])
else:
    print("Modelo não encontrado.")
