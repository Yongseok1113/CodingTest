from collections import deque


def stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)


def queue():
    queue = deque()

    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)
    queue.popleft()
    print(queue)
    queue.popleft()
    print(queue)


def recursive_func(count=0):
    if count < 4:
        print('count: ', count)
        count += 1
        recursive_func(count)


if __name__ == '__main__':
    recursive_func()