def Reverse_String(s: str) -> str:
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
