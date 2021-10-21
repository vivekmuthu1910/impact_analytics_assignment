def is_valid(combo: int, n: int):
    i = 0
    while i < n - 3:
        if not (0xF << i) & combo:
            return False
        i += 1
    return True


def generate_combination(n):
    i = 0
    while i < 2 ** n:
        if is_valid(i, n):
            yield i
        i += 1


def main():
    n = int(input("Enter total Days: ").strip())
    total = 0
    not_missed = 0
    for i in generate_combination(n):
        total += 1
        not_missed += i & 1
    print(f"{total - not_missed} / {total}")


if __name__ == "__main__":
    main()
