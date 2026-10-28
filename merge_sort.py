"""
MERGE SORT (ordenação por intercalação) - O(n log n)
Vantagens:    sempre O(n log n) (pior, médio e melhor caso); estável;
              desempenho previsível.
Desvantagens: usa memória extra O(n); é um pouco mais lento que o Quick Sort
              na prática por causa das cópias de listas.
"""
import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("merge_sort",merge_sort)
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