def example_3_1(N: int):
    answer = 0

    coin_types = (500, 100, 50, 10)
    for coin in coin_types:
        answer += N // coin
        N %= coin

    print(answer)


def practice_1():
    answer = 0
    N, M, K = map(int, input("N, M, K 입력: ").split(' '))
    numbers = map(int, input("자연수 리스트 입력: ").split(' '))

    numbers = sorted(numbers, reverse=True)
    answer += (M // (K+1)) * (numbers[0] * K + numbers[1])
    answer += (M % (K+1)) * numbers[0]

    print(answer)


def practice_2():
    answer = 0
    M, N = map(int, input("행렬 사이즈 입력 M, N: ").split(' '))
    arr = []
    for row in range(N):
        arr.append(list(map(int, input(f"{row}행 입력: ").split(' '))))

    min_value = []
    # min_index = []
    for l in arr:
        min_value.append(min(l))
        # min_index.append(l.index(min(l)))

    answer = max(min_value)
    print(answer)


def practice_3():
    answer = 0
    N, K = map(int, input("N, K 입력: ").split(' '))

    while N != 1:
        d = N % K
        if d != 0:
            answer += d
            N = N - d
        else:
            answer += 1
            N = N // K

    print(answer)


if __name__ == '__main__':
    practice_3()

