
def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: [
        spell1(*args, **kwargs), spell2(*args, **kwargs)]


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: (base_spell(*args, **kwargs) * multiplier)


def conditional_caster(condition: callable, spell: callable) -> callable:
    var = "Spell fizzled "
    return lambda *args, **kwargs: (
        spell(*args, **kwargs) if condition(*args, **kwargs) else var)


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: (spell(*args, **kwargs) for spell in spells)


def main():

    def fireball(amount):
        return amount * 10

    def ice_spike(amount):
        return amount * 8

    def heal(amount):
        return amount * 5

    def has_mana(amount):
        return amount >= 10

    def is_daytime(amount):
        return amount % 2 == 0

    print("\nTesting spell combiner...\n")
    combo_spell = spell_combiner(fireball, ice_spike)
    print("Combo Spell:", combo_spell(4))

    print("\nTesting power amplifier...\n")
    mega_fireball = power_amplifier(fireball, 3)
    print("Mega Fireball:", mega_fireball(5))

    print("\nTesting conditional caster...\n")
    safe_fireball = conditional_caster(has_mana, fireball)
    print("Safe Fireball (5 mana):", safe_fireball(5))
    print("Safe Fireball (15 mana):", safe_fireball(15))

    print("\nTesting spell sequence...\n")
    sequence = spell_sequence([fireball, ice_spike, heal])
    print("Spell Sequence:", sequence(3))

    ultimate_combo = spell_sequence([
        power_amplifier(conditional_caster(has_mana, fireball), 1),
        power_amplifier(conditional_caster(is_daytime, ice_spike), 2),
        heal])

    print("Ultimate Combo (mana=5):", ultimate_combo(9))

    print("Ultimate Combo (mana=12):", ultimate_combo(12))


if __name__ == "__main__":
    main()
