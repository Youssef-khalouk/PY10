

def mage_counter() -> callable:
    count = 0

    def func() -> int:
        nonlocal count
        count += 1
        return count
    return func


def spell_accumulator(initial_power: int) -> callable:
    count = initial_power

    def func(amount: int) -> int:
        nonlocal count
        count += amount
        return count
    return func


def enchantment_factory(enchantment_type: str) -> callable:

    def func(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return func


def memory_vault() -> dict[str, callable]:
    content = {}

    def store(key, value) -> None:
        nonlocal content
        content[key] = value

    def recall(key) -> any:
        nonlocal content
        return content.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print(f"Add 5: {accumulator(5)}")
    print(f"Add 10: {accumulator(10)}")
    print(f"Add -3: {accumulator(-3)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("level", 5)

    print("Recall spell:", vault["recall"]("spell"))
    print("Recall level:", vault["recall"]("level"))
    print("Recall missing:", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
