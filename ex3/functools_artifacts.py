import functools
import operator
from functools import lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")
    light = functools.partial(base_enchantment, power=50, element="light")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": light
    }


def memoized_fibonacci(n: int) -> int:

    @lru_cache
    def fibonacci(num: int) -> int:
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)

    return fibonacci(n)


def spell_dispatcher() -> callable:

    @singledispatch
    def cast(spell):
        return f"Unknown mystical force: {spell}"

    @cast.register
    def _(spell: int):
        return f"Fireball hits for {spell} damage!"

    @cast.register
    def _(spell: str):
        return f"Enchantment applied: {spell}"

    @cast.register
    def _(spell: list):
        results = [cast(s) for s in spell]
        return "Multi-cast activated:\n\t" + "\n\t".join(results)

    return cast


if __name__ == "__main__":

    print("\nTesting spell reducer...")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Array of Numbers: ", numbers)
    print("add     =", spell_reducer(numbers, "add"))
    print("Product =", spell_reducer(numbers, "multiply"))
    print("max     =", spell_reducer(numbers, "max"))
    print("min     =", spell_reducer(numbers, "min"))

    print("\nTesting base enchantment...")

    def base_enchantment(power, element, target):
        print(f" - power = {power}, element = {element}, target= {target}")

    enchantments = partial_enchanter(base_enchantment)
    enchantments["fire_enchant"](target="ice_enchant")
    enchantments["lightning_enchant"](target="fire_enchant")

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting dispatcher...")
    cast_spell = spell_dispatcher()

    print(cast_spell(50))
    print(cast_spell("Invisibility"))
    print(cast_spell([25, "Shield"]))
