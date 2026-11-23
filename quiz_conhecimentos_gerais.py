
import random

PERGUNTAS = [
    {"texto": "Qual e a capital do Brasil?",
     "opcoes": {"A": "Rio de Janeiro", "B": "Brasilia", "C": "Sao Paulo", "D": "Salvador"},
     "correta": "B"},
    {"texto": "Quantos planetas existem no Sistema Solar?",
     "opcoes": {"A": "7", "B": "8", "C": "9", "D": "10"},
     "correta": "B"},
    {"texto": "Quem pintou a Mona Lisa?",
     "opcoes": {"A": "Michelangelo", "B": "Van Gogh", "C": "Leonardo da Vinci", "D": "Picasso"},
     "correta": "C"},
     # kkkk perguntas sem resposta correta kkk
     {"texto": "Qual maior time do Brasil?",
     "opcoes": {"A": "Sao Paulo", "B": "Palmeiras", "C": "Vasco", "D": "Flamengo"},
     "correta": "C"},
     {"texto": "Qual maior jogador da historia?",
     "opcoes": {"A": "Cristiano Ronaldo", "B": "Messi", "C": "Pele", "D": "Neymar"},
     "correta": "A"},
     
    {"texto": "Qual e o maior oceano do mundo?",
     "opcoes": {"A": "Atlantico", "B": "Indico", "C": "Artico", "D": "Pacifico"},
     "correta": "D"},
    {"texto": "Em que ano o Brasil foi descoberto pelos portugueses?",
     "opcoes": {"A": "1500", "B": "1492", "C": "1822", "D": "1889"},
     "correta": "A"},
    {"texto": "Qual e o simbolo quimico da agua?",
     "opcoes": {"A": "O2", "B": "CO2", "C": "H2O", "D": "HO"},
     "correta": "C"},
    {"texto": "Qual e o maior animal terrestre?",
     "opcoes": {"A": "Girafa", "B": "Elefante africano", "C": "Rinoceronte", "D": "Hipopotamo"},
     "correta": "B"},
    {"texto": "Quantos estados tem o Brasil?",
     "opcoes": {"A": "24", "B": "25", "C": "26", "D": "27"},
     "correta": "C"}, 
    {"texto": "Quantas Copas do Mundo a seleção brasileira já ganhou?",
     "opcoes": {"A": "3", "B": "4", "C": "5", "D": "6"},
     "correta": "C"},
    {"texto": "Em que país aconteceu a Copa do Mundo de 2014?",
     "opcoes": {"A": "Alemanha", "B": "África do Sul", "C": "Rússia", "D": "Brasil"},
     "correta": "D"},
]

historico = []

def exibir_menu():
    print("\n" + "=" * 40)
    print("   QUIZ DE CONHECIMENTOS GERAIS")
    print("=" * 40)
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver histórico de partidas")
    print("0 - Sair")
    print("=" * 40)


def exibir_regras():
    print("\n--- REGRAS ---")
    print("• Cada partida tem 5 perguntas sorteadas.")
    print("• Responda digitando a letra da alternativa (A, B, C ou D).")
    print("• Cada acerto vale 1 ponto.")
    print("• No final, você recebe uma classificação.")


def fazer_pergunta(pergunta):
    print(f"\n{pergunta['texto']}")
    for letra, texto in pergunta["opcoes"].items():
        print(f"  {letra}) {texto}")

    resposta = input("Sua resposta: ").strip().upper()

    
    while resposta not in pergunta["opcoes"]:
        print("Opção inválida! Digite A, B, C ou D.")
        resposta = input("Sua resposta: ").strip().upper()

    if resposta == pergunta["correta"]:
        print("✔ Resposta correta!")
        return True
    else:
        letra_certa = pergunta["correta"]
        print(f"✘ Errou! A resposta certa era {letra_certa}) {pergunta['opcoes'][letra_certa]}")
        return False


def classificar(acertos, total):
    porcentagem = acertos / total * 100

    if porcentagem == 100:
        return "Gênio! Você acertou tudo!"
    elif porcentagem >= 60:
        return "Muito bom! Você mandou bem!"
    elif porcentagem >= 40:
        return "Razoável. Dá para melhorar!"
    else:
        return "Precisa estudar mais. Tente de novo!"


def jogar():
    quantidade = 5   
    sorteadas = random.sample(PERGUNTAS, quantidade)
    acertos = 0

    print("\n--- NOVA PARTIDA ---")
    for numero, pergunta in enumerate(sorteadas, start=1):
        print(f"\nPergunta {numero} de {quantidade}")
        if fazer_pergunta(pergunta):
            acertos += 1

    print("\n" + "-" * 40)
    print(f"Você acertou {acertos} de {quantidade} perguntas.")
    print(classificar(acertos, quantidade))

    historico.append(acertos)


def exibir_historico():
    print("\n--- HISTÓRICO ---")

    if len(historico) == 0:
        print("Você ainda não jogou nenhuma partida.")
        return

    for numero, acertos in enumerate(historico, start=1):
        print(f"Partida {numero}: {acertos} acertos")

    print(f"Melhor resultado: {max(historico)} acertos")


def main():
    opcao = ""

    while opcao != "0":
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            jogar()
        elif opcao == "2":
            exibir_regras()
        elif opcao == "3":
            exibir_historico()
        elif opcao == "0":
            print("\nObrigado por jogar. Até logo!")
        else:
            print("Opção inválida! Escolha um número do menu.")



if __name__ == "__main__":
    main()
