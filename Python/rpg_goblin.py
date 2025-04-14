import random
import time

# Atributos do personagem
status = {
    "dinheiro": 1000,
    "felicidade": 50,
    "amizade": 50,
    "popularidade": 50,
    "estresse": 20,
    "saude": 100
}

# Lista de eventos
EVENTOS = [
    {
        "historia": "Está chovendo forte e você dirige até o trabalho.",
        "evento": "Você perde a placa do carro.",
        "opcoes": [
            ("Ignorar e dirigir mesmo assim", {"dinheiro": -300, "estresse": +10, "saude": -10}),
            ("Comprar uma nova antes de sair", {"dinheiro": -500, "estresse": -5})
        ]
    },
    {
        "historia": "Os colegas do trabalho combinaram de não levar marmita hoje.",
        "evento": "Você decide...",
        "opcoes": [
            ("Levar marmita", {"dinheiro": 0, "amizade": -5, "felicidade": +5}),
            ("Comprar comida com eles", {"dinheiro": -40, "amizade": +10, "felicidade": +5})
        ],
        "extra": {
            "chance": 0.3,
            "evento": "Sua marmita azedou!",
            "efeito": {"saude": -10, "felicidade": -5, "dinheiro": -20}
        }
    },
    {
        "historia": "O ônibus atrasou e o chefe está de olho. Você decide...",
        "evento": "Como reagir à situação?",
        "opcoes": [
            ("Inventar desculpa", {"popularidade": -5, "estresse": +10}),
            ("Pedir desculpas", {"amizade": +5, "estresse": -5})
        ]
    },
    {
        "historia": "Hoje é dia de confraternização no trabalho.",
        "evento": "Você...",
        "opcoes": [
            ("Vai e participa ativamente", {"felicidade": +15, "amizade": +10, "dinheiro": -50}),
            ("Não vai", {"felicidade": -5, "amizade": -10})
        ]
    },
    {
        "historia": "Você encontrou uma carteira na rua.",
        "evento": "O que você faz?",
        "opcoes": [
            ("Devolve ao dono", {"popularidade": +10, "felicidade": +10}),
            ("Fica com o dinheiro", {"dinheiro": +200, "popularidade": -15})
        ]
    },
    # Adicione mais eventos aqui
]

TOTAL_DIAS = 100


def mostrar_status():
    print("\nSTATUS ATUAL:")
    for chave, valor in status.items():
        print(f"{chave.capitalize()}: {valor}")
    print("-")

def aplicar_efeitos(efeitos):
    for chave, valor in efeitos.items():
        status[chave] += valor
        status[chave] = max(0, status[chave])

def processar_evento(evento):
    print(f"\n{evento['historia']}")
    time.sleep(1.5)
    print(f"{evento['evento']}")
    for i, (texto, _) in enumerate(evento['opcoes']):
        print(f"[{i+1}] {texto}")

    while True:
        try:
            escolha = int(input("Escolha uma opção: ")) - 1
            if escolha in range(len(evento['opcoes'])):
                break
        except ValueError:
            pass
        print("Escolha inválida. Tente novamente.")

    opcao_escolhida, efeito = evento['opcoes'][escolha]
    print(f"Você escolheu: {opcao_escolhida}")
    aplicar_efeitos(efeito)
    time.sleep(1.2)

    if "extra" in evento:
        chance = evento['extra']['chance']
        if random.random() < chance:
            print(f"Evento extra: {evento['extra']['evento']}")
            aplicar_efeitos(evento['extra']['efeito'])
            time.sleep(1.2)

for dia in range(1, TOTAL_DIAS+1):
    print(f"\n\n=== DIA {dia} ===")
    eventos_do_dia = random.choices(EVENTOS, k=random.choice([0, 1, 2]))

    if not eventos_do_dia:
        print("Hoje foi um dia tranquilo. Nada de mais aconteceu.")
        time.sleep(1.5)
    else:
        for ev in eventos_do_dia:
            processar_evento(ev)

    mostrar_status()
    time.sleep(1.5)

print("\n\nParabéns! Você sobreviveu a 100 dias de CLT Journey!")1

