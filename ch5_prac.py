from collections import deque
'''
깊이 우선 탐색은 특정 방향 또는 특정 규칙으로 끝까지 반복시켜서 파고들어간다.
반복시켜서 파고들어가는 부분을 재귀함수로 구현한다.
탐색 후 분기점으로 돌아오기 위해 스택을 이용하여 노드 위치를 관리한다.

너비 우선 탐색은 현재 위치에서 가까운 주변을 모두 확인하면서 서서히 확장해나간다.
목적을 달성할때까지 반복하면서 주변을 확인한다. 
탐색 후 분기점으로 돌아오기 위해 큐를 이용하여 노드 위치를 관리한다.


'''

def ice_beverage():
    n, m = map(int, input("행열 값 입력: ").split(' '))

    map_data = []
    for i in range(n):
        map_data.append(list(map(int, input("맵 정보 입력: ").split(' '))))

    # 노드정보, 노드 방문여부, 시작 위치
    def dfs(x, y):
        # x 나 y 가 맵 경계를 넘으면 중지
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

        if map_data[x][y] == 0:
            map_data[x][y] = 1

            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    result = 0
    for row in range(n):
        for col in range(m):
            if dfs(row, col):
                result += 1

    print(result)


def maze_escape():
    answer = 0
    n, m = map(int, input("행렬 값 입력: ").split(' '))
    map_data = []
    for row in range(n):
        map_data.append(list(map(int, input("맵 정보 입력: "))))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for xd, yd in zip(dx, dy):
                nx = x + xd
                ny = y + yd
                # 미로 공간 벗어날 경우 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 벽이면 무시
                elif map_data[nx][ny] == 0:
                    continue
                # 1일때만 증가시키면 재방문에 대해 증가시키지 않으므로 최단거리 가능
                # 한 스텝에 4가지 방향에 대해 모두 경우를 확인하여 큐에 삽입하므로 막다른길은 자연히 해당 위치 큐를 소비하면서 이전에
                # 주변에 1을 모두 제거했기 때문에 아무것도 없이 소멸됨(작업만 소모)

                elif map_data[nx][ny] == 1:
                    # 중요: 다음 목적지에 이전 목적지 값 + 1을 할당하고 큐에 저장
                    # 이전 목적지 값 + 1은 현재까지 이동한 스텝 수
                    map_data[nx][ny] = map_data[x][y] + 1
                    queue.append((nx, ny))

        return map_data[n-1][m-1]  # 목적지에 있는 최단거리 값 반환

    answer = bfs(0, 0)
    print(answer)


if __name__ == "__main__":
    maze_escape()
