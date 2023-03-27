#Решето Эратосфера (алгоритм, который ищет все простые числа до заданного целого числа
#https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%AD%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0

N = int(input())
A = [True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
for k in range(N):
    if A[k]:
        print(k, '-', "простое" if A[k] else "составное") #здесь используется проверка условия прямо в ф-ии принта