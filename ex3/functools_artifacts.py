import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add , spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> callable:
    pass


if __name__ == "__main__":
    print(spell_reducer([1,2,3,4,5], "add"))
    print(spell_reducer([1,2,3,4,5], "multiply"))
    print(spell_reducer([1,2,3,4,5], "max"))
    print(spell_reducer([1,2,3,4,5], "min"))
