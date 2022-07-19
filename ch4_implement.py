def example_4_1():
    answer = [1, 1]
    N = int(input("맵 크기: "))
    plan = input("계획서: ").split(' ')
    for step in plan:
        if step == "L":
            if answer[1] > 1:
                answer[1] -= 1
        elif step == "R":
            if answer[1] < N:
                answer[1] += 1
        elif step == "U":
            if answer[0] > 1:
                answer[0] -= 1
        elif step == "D":
            if answer[0] < N:
                answer[0] += 1

    print(answer)


if __name__ == "__main__":
    example_4_1()