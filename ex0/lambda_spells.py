

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
    }


def main():

    print("Testing artifact sorter...\n")
    artifacts = [
        {'name': 'Earth Shield', 'power': 104, 'type': 'focus'},
        {'name': 'Wind Cloak', 'power': 67, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 109, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 62, 'type': 'accessory'}
    ]
    arts = artifact_sorter(artifacts)
    for art in arts:
        print(f"name: {art["name"]}, power = {art["power"]}, type: {art["type"]}")

    print("\nTesting spell transformer...\n")

    spells = ['tornado', 'meteor', 'heal', 'shield']
    spl = spell_transformer(spells)
    for s in spl:
        print(s, end=" ")

        
    print("\n\nTesting mage status...\n")
    mages = [
        {'name': 'Luna', 'power': 97, 'element': 'earth'},
        {'name': 'Riley', 'power': 77, 'element': 'ice'},
        {'name': 'Kai', 'power': 61, 'element': 'wind'},
        {'name': 'Riley', 'power': 59, 'element': 'water'},
        {'name': 'Phoenix', 'power': 94, 'element': 'earth'}
    ]

    art = mage_stats(mages)

    print(f"max_power={art["max_power"]}, min_power={art["min_power"]}, avg_power={art["avg_power"]}")


if __name__ == "__main__":
    main()
