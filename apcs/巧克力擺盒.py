from itertools import permutations
from functools import lru_cache

flavors = ["P", "B", "Y"]  # Strawberry, Original, Coffee
shapes = ["S", "C", "T"]  # Square, Circle, Triangle

chocolates = tuple((f, s) for f in flavors for s in shapes)


@lru_cache(maxsize=None)
def check_single_condition(row, condition):
    if len(condition) == 2:  # where only 2 chocolates are specified
        return all(
            (cf == "?" or cf == rf) and (cs == "?" or cs == rs)
            for (cf, cs), (rf, rs) in zip(condition, row[:2])
        ) or all(
            (cf == "?" or cf == rf) and (cs == "?" or cs == rs)
            for (cf, cs), (rf, rs) in zip(condition, row[1:])
        )
    else:
        return all(
            (cf == "?" or cf == rf) and (cs == "?" or cs == rs)
            for (cf, cs), (rf, rs) in zip(condition, row)
        )


def check_condition(perm, condition):
    return any(
        check_single_condition(perm[i * 3 : (i + 1) * 3], condition) for i in range(3)
    )


def count_arrangements(conditions):
    count = 0
    for perm in permutations(chocolates):
        if all(check_condition(perm, cond) for cond in conditions):
            count += 1
    return count


def main():
    N = int(input())
    conditions = []

    for _ in range(N):
        line = input().split()
        cond = tuple((line[i], line[i + 1]) for i in range(1, len(line), 2))
        conditions.append(cond)

    result = count_arrangements(conditions)
    print(result)


if __name__ == "__main__":
    main()
