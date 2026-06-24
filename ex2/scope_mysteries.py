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
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> Any:
        try:
            return memory[key]
        except KeyError:
            return ("Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    spell_acc = spell_accumulator(100)
    flaming_ent = enchantment_factory("Flaming")
    frozen_ent = enchantment_factory("Frozen")
    mem = memory_vault()

    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    print(f"Base 100, add 20: {spell_acc(20)}")
    print(f"Base 100, add 30: {spell_acc(30)}")

    print("\nTesting enchantment factory...")
    print(flaming_ent("Sword"))
    print(frozen_ent("Shield"))

    print("\nTesting memory vault...")
    print("Store 'secret' = 42")
    mem['store']("secret", 42)
    print(f"Recall 'secret': {mem['recall']('secret')}")
    print(f"Recall 'unknown': {mem['recall']('unknown')}")



