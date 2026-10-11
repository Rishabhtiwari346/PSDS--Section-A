def solve(N, A):
    positive = 0
    negative = 0

    for x in A:
        if x > 0:
            positive += x
        elif x < 0:
            negative += x

    total = positive + negative

    if total > 0:
        return -1

    if 2 * positive > -negative:
        return -1

    return -total


data = input().split()

T = int(data[0])
index = 1

for _ in range(T):
    N = int(data[index])
    index += 1

    A = list(map(int, data[index:index + N]))
    index += N

    print(solve(N, A))
