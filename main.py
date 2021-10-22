from functools import lru_cache

CONSEC_DAYS = 4


@lru_cache(maxsize=100)
def count_invalids(n: int):
    if n < CONSEC_DAYS:
        return 0
    if n == CONSEC_DAYS:
        return 1
    total = 0
    for i in range(n - CONSEC_DAYS + 1):
        current_values = 1
        if i < n - CONSEC_DAYS:
            current_values *= 2 ** (n - CONSEC_DAYS - i)
        if i > 1:
            current_values *= (2 ** (i - 1)) - count_invalids(i - 1)
        total += current_values
    return total


def main():
    try:
        n = int(input("Enter total days: ").strip())
    except ValueError:
        print("Enter a valid number")
        exit(1)
    total = 2 ** n
    valid = 2 ** n - count_invalids(n)
    missed = int(total / 2)
    missed -= count_invalids(n - 1)
    if n == CONSEC_DAYS:
        missed -= 1
    elif n > CONSEC_DAYS:
        missed -= 2 ** (n - CONSEC_DAYS - 1) - count_invalids(n - CONSEC_DAYS - 1)
    print(f"{missed} / {valid}")


if __name__ == "__main__":
    main()
