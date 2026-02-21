

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


a = 100

def memory_vault() -> dict[str, callable]:
    content = {}


    def store(key, value) -> None:
        nonlocal content
        global a

        print

        content[key] = value

    def recall(key) -> any:
        nonlocal content
        return content.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")

    var = memory_vault()

    var["store"]("name", "youssef")
    print(var["recall"]("name"))
    print(var["recall"]("age"))

    print(variable)

if __name__ == "__main__":
    main()
