'''
Para o termo, usaremos cores para indicar se a letra está correta e na posição correta (verde), 
se a letra está correta mas na posição errada (amarelo) ou se a letra está incorreta (branco).
As regras são as mesmas do site. O jogador tem 6 tentativas para adivinhar a palavra.
'''


import random
from termcolor import colored


'''
Usamos a função random.choice() para escolher uma palavra da lista de palavras.
Para seguir as regras do termo, a palavra deve ter 5 letras.
'''
def escolher_palavra():
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo.readlines() if len(linha.strip()) == 5]

    return random.choice(palavras)


'''
A função verificar_palavra() recebe a palavra a ser adivinhada e conta as tentativa do jogador.
'''
def verificar_palavra(palavra_secreta, tentativa):
    resultado = []
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == tentativa[i]:
            resultado.append(colored(tentativa[i], 'green'))
        elif tentativa[i] in palavra_secreta:
            resultado.append(colored(tentativa[i], 'yellow'))
        else:
            resultado.append(tentativa[i])
    return resultado

'''
A função principal é onde inicializamos a palavra secreta e o número de tentativas.

'''
def jogar():
    palavra_secreta = escolher_palavra()
    tentativas = 6

    print(f"Term.ooo - Adivinhe a palavra secreta de 5 letras em até {tentativas} tentativas")

    # Enquanto houverem tentativas, o jogo continua
    while tentativas > 0:
        tentativa = input("Digite uma palavra: ").strip().lower()

        if len(tentativa) != 5 or not tentativa.isalpha():
            print("A palavra deve ter 5 letras.")
            continue

        resultado = verificar_palavra(palavra_secreta, tentativa)

        print(" ".join(resultado))
        
        if palavra_secreta == tentativa:
            print("\nParabéns, você adivinhou a palavra: " + palavra_secreta)
            break

        tentativas -= 1

    if palavra_secreta != tentativa:
        print("\nVocê perdeu, a palavra era: " + palavra_secreta)


if __name__ == "__main__":
    jogar()
