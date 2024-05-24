# Jogo da forca

import random

def escolher_palavra():
    palavras = ['celular', 'computador', 'televisao']
    return random.choice(palavras)

def mostrar_tabuleiro(palavra, letras_certas):
    tabuleiro = ''
    for letra in palavra:
        if letra in letras_certas:
            tabuleiro += letra
        else:
            tabuleiro += '_'
    return tabuleiro

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    tentativas = 6
    print('Salve Thier, quero ver tu acertar a palavra!')

    while tentativas > 0:
        print(mostrar_tabuleiro(palavra, letras_certas))
        palpite = input('Vamos lá! Escolha uma letra de A-Z: ').lower()

        if palpite in palavra and palpite not in letras_certas:
            letras_certas.append(palpite)
            print('Boa chefe, acertou!')
        else:
            tentativas -= 1
            print(f'Vish, deu ruim! Você tem {tentativas} tentativas restantes.')

        if set(letras_certas) == set(palavra):
            print(f'Parabéns Thier! Você descobriu a palavra: {palavra}')
            break
    else:
        print(f'Fim de jogo! A palavra era: {palavra}')

if __name__ == '__main__':
    jogar_forca()
