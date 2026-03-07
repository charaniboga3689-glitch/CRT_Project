def number_triangle(n: int) -> str:
    pattern = []
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        pattern.append(line)
    return "\n".join(pattern)

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))