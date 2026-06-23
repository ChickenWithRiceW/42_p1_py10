from collections.abc import Callable
from typing import Any

def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable:
    def count(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power
    return count


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment
    # Could also be just a line of a lambda
    # return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> dict:
        try:
            return memory[key]
        except KeyError as e:
            print(e)
    return {"store": store, "recall": recall}



if __name__ == "__main__":
    test = memory_vault()
    test["store"]("Rank", 2)
    print(test["recall"]("Rank"))
