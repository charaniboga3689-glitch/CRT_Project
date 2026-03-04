from typing import List


def Collatz_Sequence(n: int) -> List:
    sequence = []

    while True:
        sequence.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    return sequence


if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))
