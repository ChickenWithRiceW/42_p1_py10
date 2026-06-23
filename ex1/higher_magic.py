from collections.abc import Callable


# I guess like this? I mean Idk
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda t0, p0: (spell1(t0, p0), spell2(t0, p0))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda t0, p0: base_spell(t0, p0 * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda t0, p0: spell(t0, p0) if condition(t0, p0)\
            else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda t0, p0: [spell(t0, p0) for spell in spells]


# Spells --------------------------------------------
def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def stun(target: str, power: int) -> str:
    return f"{target} got stunned for {power} seconds"


def con(target: str, _: int):
    return True if target[0] == 'A' else False


if __name__ == "__main__":

    heal_with_stun = spell_combiner(heal, stun)
    heal_amplified = power_amplifier(heal, 2)
    heal_conditional = conditional_caster(con, heal)
    spell_sequence_val = spell_sequence([heal, stun])

    print(heal_with_stun("Paul", 10))
    print(heal_amplified("Herbert", 10))

    print(heal_conditional("Herbert", 12))
    print(heal_conditional("Albert", 12))

    print(spell_sequence_val("herbert", 20))
