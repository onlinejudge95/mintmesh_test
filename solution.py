from itertools import combinations


COUNT = 0


def _get_subsets(array: list, data: list, start: int, end: int, index: int, size: int):
    if index == size:
        if sum(data[:size]) <= 1000:
            global COUNT
            COUNT += 1
        return

    i = start
    while i <= end and end - i + 1 >= size - index:
        data[index] = array[i]
        _get_subsets(array, data, i + 1, end, index + 1, size)
        i += 1


def solve(array: list, size: int) -> None:
    data = [0] * size

    _get_subsets(array, data, 0, len(array) - 1, 0, size)

    print(COUNT)


if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())

    solve(A, B)
