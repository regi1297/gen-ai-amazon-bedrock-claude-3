import sys

def recomendar_modelo(desempenho, velocidade, custo, capacidades):
    capacidades = [cap.strip().lower() for cap in capacidades.split(",")]

    # Critérios para cada modelo Claude 3
    modelos = {
        "Claude 3 Opus": {
            "desempenho": 9,
            "velocidade": 10,
            "custo": 5,
            "capacidades": ["pesquisa", "desenvolvimento acelerado"]
        },
        "Claude 3 Sonnet": {
            "desempenho": 8,
            "velocidade": 5,
            "custo": 7,
            "capacidades": ["codificação", "recuperação de informações"]
        },
        "Claude 3 Haiku": {
            "desempenho": 7,
            "velocidade": 9,
            "custo": 6,
            "capacidades": ["velocidade", "resumo de dados não estruturados"]
        }
    }

    # Checar cada modelo
    for modelo, criterios in modelos.items():
        if (desempenho >= criterios["desempenho"] and
            velocidade >= criterios["velocidade"] and
            custo <= criterios["custo"] and
            any(cap in capacidades for cap in criterios["capacidades"])):
            return f"O {modelo} é o modelo recomendado."

    return "Nenhum modelo encontrado."

# Leitura das entradas
desempenho = int(sys.stdin.readline().strip())
velocidade = int(sys.stdin.readline().strip())
custo = int(sys.stdin.readline().strip())
capacidades = sys.stdin.readline().strip()

# Recomendação do modelo
resultado = recomendar_modelo(desempenho, velocidade, custo, capacidades)

# Saída do resultado
print(resultado)
