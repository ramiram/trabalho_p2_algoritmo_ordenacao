"""
RADIX SORT (LSD, base 10) - O(d · (n + b)), d = nº de dígitos, b = base
Vantagens:    não usa comparações; muito eficiente para inteiros com poucos
              dígitos; estável.
Desvantagens: limitado a inteiros/strings (aqui, não negativos); usa memória
              extra; depende do nº de dígitos dos valores.
"""
import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO

def radix_sort(lista):
    if not lista:
        return lista
    maior = max(lista)
    exp = 1
    while maior // exp > 0:
        lista = _counting_por_digito(lista, exp)
        exp *= 10
    return lista


def _counting_por_digito(lista, exp):
    contagem = [0] * 10
    for x in lista:
        contagem[(x // exp) % 10] += 1
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    saida = [0] * len(lista)
    for x in reversed(lista):
        d = (x // exp) % 10
        contagem[d] -= 1
        saida[contagem[d]] = x
    return saida

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("radix_sort",radix_sort)
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