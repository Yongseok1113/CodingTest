from collections import deque

array = [2, 4, 5, 1, 3, 9]


def quick_sort(array, pivot):
    """
        내가 푼 함수가 제대로 동작하지 않는 이유
        함수에 전달하는 array 를 슬라이스 하면서
        pivot = small_idx에서 인덱스가 잘못되기 때문
        인덱스 괴리를 해결하던가 원본을 자르지 않던가 해야한다.
    """
    large_idx = 0
    small_idx = 0
    if len(array) == 1 or not array:
        return

    while True:
        for idx in range(pivot, len(array), 1):
            if array[idx] > array[pivot]:
                large_idx = idx
                break

        for idx in range(len(array) - 1, pivot, -1):
            if array[idx] < array[pivot]:
                small_idx = idx
                break

        if large_idx > small_idx:
            array[pivot], array[small_idx] = array[small_idx], array[pivot]
            pivot = small_idx
            print("pivot: ", pivot)
            break
        else:
            array[large_idx], array[small_idx] = array[small_idx], array[large_idx]

    quick_sort(array[:pivot], 0)
    quick_sort(array[pivot + 1:], 0)


def quick_sort_answer1(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort_answer1(array, start, right-1)
    quick_sort_answer1(array, right+1, end)


# python 스럽게 짜여져 있지만 속도는 answer1보다 느림
def quick_sort_answer2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # pivot 을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick_sort_answer2(left_side) + [pivot] + quick_sort_answer2(right_side)


def practice1():
    answer = 0
    l1 = []
    n = int(input("수열 요소 개수: "))
    for _ in range(n):
        l1.append(int(input("수 입력: ")))

    answer = sorted(l1, reverse=True)
    print(answer)


def practice2():
    n = int(input("학생 수: "))
    students = []
    for _ in range(n):
        name, score = input("학생 이름과 성적 입력").split(' ')
        students.append((name, int(score)))

    def key_func(data):
        return data[1]

    students = sorted(students, key=key_func)

    print(students)


def practice3():
    n, k = map(int, input("배열 수, 교체 횟수 입력: ").split(' '))

    a = list(map(int, input("배열 a 입력: ").split(' ')))
    b = list(map(int, input("배열 b 입력: ").split(' ')))

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:  # 정렬을 했는데 a보다 b가 작으면 이 후 모두 같은 상황 이므로 굳이 모두 확인할 필요가 없음
            break

    print(sum(a))






if __name__ == "__main__":
    # quick_sort(array, 0)
    # quick_sort_answer1(array, 0, len(array)-1)
    # print(array)

    # print(quick_sort_answer2(array))

    practice3()


