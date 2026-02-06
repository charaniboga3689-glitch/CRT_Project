def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = (n1 + n2 + n3) / 3

    # conditional formatting
    if average.is_integer():
        avg_str = f"{average:.1f}"
    else:
        avg_str = f"{average:.2f}"

    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))
