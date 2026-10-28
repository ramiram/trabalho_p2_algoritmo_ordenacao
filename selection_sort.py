"""
SELECTION SORT (ordenação por seleção) - O(n²)
Vantagens:    simples; faz poucas trocas (no máximo n-1); usa pouca memória O(1).
Desvantagens: sempre O(n²), mesmo com lista já ordenada; muito lento para
              listas grandes; não é estável.
"""
import random
import time

TAMANHO = 100_000      # quantidade de elementos da lista
VALOR_MAXIMO = 100_000 # valores aleatórios entre 0 e VALOR_MAXIMO

def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("selection_sort",selection_sort)
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