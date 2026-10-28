"""
COUNTING SORT (ordenação por contagem) - O(n + k), k = amplitude dos valores
Vantagens:    não usa comparações; muito rápido quando k é pequeno em relação
              a n; estável.
Desvantagens: só funciona com inteiros (ou chaves inteiras); gasta memória
              O(k), inviável se a amplitude dos valores for muito grande.
"""
import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO

def counting_sort(lista):
    if not lista:
        return lista
    menor, maior = min(lista), max(lista)
    contagem = [0] * (maior - menor + 1)
    for x in lista:
        contagem[x - menor] += 1
    # soma acumulada: posição final de cada valor
    for i in range(1, len(contagem)):
        contagem[i] += contagem[i - 1]
    saida = [0] * len(lista)
    for x in reversed(lista):  # percorrer de trás para frente mantém a estabilidade
        contagem[x - menor] -= 1
        saida[contagem[x - menor]] = x
    return saida

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("counting_sort", counting_sort)
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