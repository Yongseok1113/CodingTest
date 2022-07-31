array = [1, 2, 4, 6, 7, 8, 11, 23]


# 이진 탐색은 정렬된 배열에서 사용 가능하다.
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, end)
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)
    else:
        print("something wrong!")
    return None


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            print("something wrong!")
    return None


# 빠르게 입려 받기
# 보통 이진 트리 탐색 구현 문제는 잘 나오지 않지만 이진 탐색은 데이터가 큰 형태로 주로 나옴
# input 함수는 느려서 시간초과 발생할 수 있으니 sys 모듈의 readline 함수를 이용한다.
import sys
def fast_input():
    input_data = sys.stdin.readline().rstrip()
    print(input_data)


# 이진 탐색트리는 자식노드가 2개씩 생성되면서 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드 가 모든 노드에 대해 성립하는 트리를 말함
def binary_tree_search():
    n = int(sys.stdin.readline().rstrip())
    n_data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    m = int(sys.stdin.readline().rstrip())
    m_data = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    n_data.sort()
    m_data.sort()

    results = []
    for i in m_data:
        if binary_search(n_data, i, 0, len(n_data) - 1):
            results.append('yes')
        else:
            results.append('no')

    return results


if __name__ == "__main__":
    target = 6
    # print(array[binary_search_recursive(array, target, 0, len(array)-1)])
    # print(array[binary_search(array, target, 0, len(array)-1)])
    print(binary_tree_search())







if __name__ == "__main__":
    pass

