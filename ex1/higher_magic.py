from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda t, p: (spell1(t, p), spell2(t, p))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda t, p: base_spell(t, p * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda t, p: spell(t, p) if condition(t, p) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda t, p: [spell(t, p) for spell in spells]


def heal(target: str, power: int) -> str:
    return f"{target}'s health got restored for {power} HP"


def stun(target: str, power: int) -> str:
    return f"{target} got stunned for {power} seconds"


def con(target: str, _: int) -> bool:
    return True if target[0] == 'A' else False


if __name__ == "__main__":

    heal_with_stun = spell_combiner(heal, stun)
    heal_amplified = power_amplifier(heal, 3)
    heal_conditional = conditional_caster(con, heal)
    spell_sequence_val = spell_sequence([heal, stun])

    print("Testing spell combiner...\nCombined spell result: ", end='')
    print(*heal_with_stun("Paul", 10), sep=', ')

    print("\nTesting power amplifier...\nOriginal: 10, Amplified: 30")
    print(heal_amplified("Herbert", 10))

    print("\nTesting spell conditional...")
    print(f"Condition not met: {heal_conditional('Herbert', 12)}")
    print(f"Condition met: {heal_conditional('Albert', 12)}")

    print("\nTesting spell sequence...")
    print(*spell_sequence_val("Herbert", 20), sep=" and ")
