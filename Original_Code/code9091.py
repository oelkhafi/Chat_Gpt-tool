N = int(input())
A = list(map(int, input().split()))
memo = [None] * (N + 1)


def step_sum(stairs: list, i):  # начинаем c -1 до i-той ступеньки
    if i == 1:
        return stairs[0]
    if i == 0:
        return 0
    if memo[i] is not None:
        return memo[i]
    r1 = step_sum(stairs, i - 1)
    memo[i - 1] = r1
    r2 = step_sum(stairs, i - 2)
    memo[i - 2] = r2
    return max(r1, r2) + stairs[i - 1]   # максимум из 2х подазадач
                                         # + стоимость текущей ступеньки

print(step_sum(A, N))
 