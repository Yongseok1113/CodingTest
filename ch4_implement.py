
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


def knight():
    '''
        8x8 좌표 체스판
        수평 두칸 + 수직 한칸 or 수직 두칸 + 수평 한칸
        가능한 경우의 수
        행: 1~8, 열: a~h

        입력예 : a1 -> 가능한 경우의수 c2, b3 두개
    :return:
    '''
    answer = 0
    init_loc = input("나이트 위치: ")
    col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = int(init_loc[1]) - 1
    y = col.index(init_loc[0])
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for step in steps:
        next_row = x + step[0]
        next_col = y + step[1]
        if 0 <= next_row <= 7 and 0 <= next_col <= 7:
            answer += 1

    print(answer)


def game_develop():
    direction_table = {i: v for i, v in enumerate([[0, -1], [0, 1], [1, 0], [-1, 0]])}

    answer = 0
    input_data = input("맵 행렬 크기 입력: ")  # 4 4
    row, col = map(int, input_data.split(' '))

    input_data = input("현재위치 A B와 방향 D 입력: ")  # 1 1 0
    a, b, d = list(map(int, input_data.split(' ')))
    current_loc = [a, b]
    current_direction= d

    game_map = []
    for r in range(row):
        input_data = input("맵 지형 입력: ")
        game_map.append(list(map(int, input_data.split(' '))))
    ''' 
        입력 맵
        1 1 1 1
        1 0 0 1
        1 1 0 1
        1 1 1 1
    '''
    turn_time = 0
    while True:
        if turn_time == 4:
            current_loc = list(map(lambda x, y: x + y, current_loc, direction_table[(current_direction + 2) % 4]))
            if game_map[current_loc[0]][current_loc[1]] != 0:
                break
            turn_time = 0

        if game_map[current_loc[0]][current_loc[1]] == 0:
            game_map[current_loc[0]][current_loc[1]] = 2
            answer += 1
            continue
        else:
            check = direction_table[current_direction]
            temp_loc = list(map(lambda x, y: x + y, current_loc, check))
            if game_map[temp_loc[0]][temp_loc[1]] == 0:
                current_loc = temp_loc
            else:
                current_direction = current_direction - 1 if current_direction > 0 else 3
                turn_time += 1

    print(answer)  # 3


if __name__ == "__main__":
    game_develop()
