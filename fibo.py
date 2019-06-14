def fibo():
    n = int(input('podaj n'))
    tablica = [0, 1]
    for i in range(2, n + 1):
        tablica.append(tablica[i - 2] + tablica[i - 1])
    return tablica[n]


print(fibo())