"""
QUICK SORT (ordenação rápida) - O(n log n) médio, O(n²) no pior caso
Vantagens:    geralmente o mais rápido na prática; in-place (pouca memória
              extra); boa localidade de cache.
Desvantagens: pior caso O(n²) com pivôs ruins (aqui reduzido com pivô
              aleatório); não é estável; recursão pode ficar profunda.
"""
import random
import time

TAMANHO = 100_000       # quantidade de elementos da lista
VALOR_MAXIMO = 100_000  # valores aleatórios entre 0 e VALOR_MAXIMO


def quick_sort(lista):
    _quick(lista, 0, len(lista) - 1)
    return lista


def _quick(lista, baixo, alto):
    while baixo < alto:
        # pivô aleatório evita o pior caso em listas já ordenadas
        indice_pivo = random.randint(baixo, alto)
        lista[indice_pivo], lista[alto] = lista[alto], lista[indice_pivo]
        pivo = lista[alto]

        i = baixo - 1
        for j in range(baixo, alto):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        p = i + 1

        # recursão na parte menor, laço na maior (limita a profundidade)
        if p - baixo < alto - p:
            _quick(lista, baixo, p - 1)
            baixo = p + 1
        else:
            _quick(lista, p + 1, alto)
            alto = p - 1

def main():
    original = [random.randint(0, VALOR_MAXIMO) for _ in range(TAMANHO)]
    esperado = sorted(original)
    print(f"Lista aleatória com {TAMANHO:,} elementos criada.\n".replace(",", "."))

    algoritmos = [
        ("quick_sort", quick_sort)
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
