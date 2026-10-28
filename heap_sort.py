"""
HEAP SORT - O(n log n)
Vantagens:    sempre O(n log n); in-place (memória O(1)); não tem pior caso
              quadrático.
Desvantagens: não é estável; na prática costuma ser mais lento que Quick Sort
              e Merge Sort; acessos à memória pouco sequenciais.
"""

import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO


def heap_sort(lista):
    n = len(lista)

    def peneirar(tamanho, raiz):
        while True:
            maior = raiz
            esq = 2 * raiz + 1
            dir_ = 2 * raiz + 2
            if esq < tamanho and lista[esq] > lista[maior]:
                maior = esq
            if dir_ < tamanho and lista[dir_] > lista[maior]:
                maior = dir_
            if maior == raiz:
                return
            lista[raiz], lista[maior] = lista[maior], lista[raiz]
            raiz = maior

    # constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        peneirar(n, i)
    # extrai o maior elemento repetidamente
    for fim in range(n - 1, 0, -1):
        lista[0], lista[fim] = lista[fim], lista[0]
        peneirar(fim, 0)
    return lista

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("heap_sort",heap_sort)
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