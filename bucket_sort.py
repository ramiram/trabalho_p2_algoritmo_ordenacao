"""
BUCKET SORT (ordenação por baldes) - O(n + k) médio, O(n²) no pior caso
Vantagens:    muito rápido quando os valores são bem distribuídos
              (uniformes); fácil de paralelizar.
Desvantagens: desempenho cai se muitos elementos caírem no mesmo balde; usa
              memória extra; depende da distribuição e da escolha dos baldes.
"""

from insertion_sort import insertion_sort
import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO


def bucket_sort(lista):
    if not lista:
        return lista
    menor, maior = min(lista), max(lista)
    qtd_baldes = max(1, len(lista) // 10)
    amplitude = (maior - menor + 1) / qtd_baldes
    baldes = [[] for _ in range(qtd_baldes)]
    for x in lista:
        baldes[int((x - menor) / amplitude)].append(x)

    resultado = []
    for balde in baldes:
        insertion_sort(balde)  # cada balde é pequeno, então Insertion Sort é eficiente
        resultado.extend(balde)
    return resultado

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("bucket_sort",bucket_sort)
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