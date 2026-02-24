import time
import functools
from typing import Any


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.6f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str | Any:
            power = kwargs.get("power", None)
            if not power:
                power = args[0] if args else None
            if power and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt = 0
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"({attempt}/{max_attempts})")
                    else:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        count = 0
        for i in range(1000):
            count += 1
        return "Fireball cast!"
    result = fireball()
    print("Result:", result)

    print("\nTesting power validator")

    @power_validator(50)
    def cast_spell(power, spell_name):
        return f"{spell_name} cast with power {power}!"

    print(cast_spell(55, "ice_spell"))
    print(cast_spell(45, "ice_spell"))

    print("\nTesting retry spell...")

    counter = 0

    @retry_spell(3)
    def unstable_spell():
        global counter
        counter += 1
        if counter < 3:
            raise ValueError("Spell fizzled!")
        return "Spell cast successfully!"

    print(unstable_spell())

    print("\nTesting MageGuild...")

    mage = MageGuild()

    print(mage.validate_mage_name("alpha"))
    print(mage.validate_mage_name("alpha1"))
    print(mage.cast_spell(spell_name="Lightning", power=15))
    print(mage.cast_spell(spell_name="Lightning", power=5))
