def sum_of_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))