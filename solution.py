from itertools import combinations


# Global variable to store the count
# It's not a good idea I understand.
COUNT = 0


def _get_subsets(array: list, data: list, start: int, end: int, index: int, size: int):
    """
    Recursive utiltiy method to find the subsets with a given length.
    Once the subset matches check if the sum is less than or equal to 1000
    If yes bump the count by 1
    """
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
    """
    Driver function to call the recursive function and print the count for the same.
    """
    data = [0] * size

    _get_subsets(array, data, 0, len(array) - 1, 0, size)

    print(COUNT)


if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = int(input())

    solve(A, B)
