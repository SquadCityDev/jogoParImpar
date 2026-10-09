import random

def par_impar():
    print("=" * 40)
    print(" Bem-vindo ao Jogo Par ou ímpar")
    print("=" * 40)

    vitorias_usuario = 0
    vitorias_ia = 0

    while True:
        escolha_usuario = input("\nEscolha [P]ar ou [Í]mpar - S para sair").strip().upper()

        if escolha_usuario == 'S':
          print ("\nSaindo do jogo...")
          break

        if escolha_usuario not in["P","Í","I" ]:
           print("Opção Inválida, Digite P ou I")
           continue

        if escolha_usuario == "Í":
           escolha_usuario ="I"

        try:
           numero_usuario=int(input("Digite um número inteiro"))
        except ValueError:
           print("Por apenas numeros inteiros")
           continue

        # A IA escolhe o numero
        numero_ia = random.randint(0, 10)

        soma = numero_usuario + numero_ia
        resultado = "P" if soma % 2 == 0 else "I"

        # Linha divisória
        print("_" * 40)
        print(f"Você jogou {numero_usuario} e a IA jogu {numero_ia}")
        print(f"A soma foi {soma} ({"PAR" if resultado =="P" else "ÍMPAR"}).")

        if escolha_usuario == resultado:
            print("Parabéns! Você ganhou está rodada")
        else:
           print("A IA ganhou está rodada")
           vitorias_ia += 1 

        print(f"Placar Atual -> Você: {vitorias_usuario} | IA: {vitorias_ia}")

        print("\n" + "=" * 40)
        print("Fim de jogo placar Final:")
        print(f"Você: {vitorias_usuario} Vitórias")
        print(f"IA: {vitorias_ia} vitórias")
        print("Obrigado por Jogar")
        print("=" * 40)

if __name__ =="__main__":
    par_impar()

