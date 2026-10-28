"""
BUBBLE SORT - O(n²) (melhor caso O(n) com a verificação de "trocou")
Vantagens:    muito simples; estável; detecta lista já ordenada (melhor caso O(n)).
Desvantagens: faz muitas comparações e trocas; é o mais lento dos algoritmos
              comuns; inviável para listas grandes.
"""

import random
import time

TAMANHO = 100_000      # quantidade de elementos da lista
VALOR_MAXIMO = 100_000 # valores aleatórios entre 0 e VALOR_MAXIMO

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:  # nenhuma troca: a lista já está ordenada
            break
    return lista

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("bubble_sort",bubble_sort)
    ]

    print(f"{'Algoritmo':<16}{'Tempo (s)':>12} Ordenou corretamente")
    print("-" * 52)
    for nome, funcao in algoritmos:
        copia = original.copy()  # cada algoritmo recebe a mesma lista
        inicio = time.perf_counter()
        resultado = funcao(copia)
        tempo = time.perf_counter() - inicio
        correto = "Sim" if resultado == esperado else "NAO"
        print(f"{nome:<16}{tempo:>12.4f}         {correto}")

    # print("")
    # print(original) #exiba a lista aleatoria
    # print("")
    # print(resultado) #exibe a lista ordenada


if __name__ == "__main__":
    main()