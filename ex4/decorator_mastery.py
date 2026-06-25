from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


# This layer is for configuring the decorator ergo min_power
def power_validator(min_power: int) -> Callable:
    # print(f"Setting up env for decorator. min_power = {min_power}")

    # This is the actual decorator like spell_timer above
    def decorator(func: Callable) -> Callable:
        # print(f"Setting up decorator. callable func val = {func.__name__}")

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            # Needs keyword argument for method in class
            power = kwargs.get("power", args[0])
            # print("Now the actual wrapper logic")
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == max_attempts:
                        return (f"Spell casting failed after {i} attempts")
                    print("Spell failed, retrying... "
                          f"(attempt {i}/{max_attempts})")
        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.122)
    return "Fireball cast!"


@retry_spell(3)
def scream_spell() -> str:
    return "Waaaaaaagh spelled !"


@retry_spell(3)
def fail_spell() -> str:
    raise Exception("Failing for the fun of it")


if __name__ == "__main__":

    print("\nTesting spell timer...")

    print("Result:", fireball())

    print("\nTesting retrying spell...")

    print(fail_spell())

    print(scream_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Kai"))
    print(MageGuild.validate_mage_name("Ka"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))
