def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": round(sum(i["power"] for i in mages) / len(mages), 2)
    }


if __name__ == "__main__":

    # Lambda Sanctum Test Data
    artifacts = [{'name': 'Earth Shield', 'power': 97, 'type': 'accessory'},
                 {'name': 'Shadow Blade', 'power': 84, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 97, 'type': 'armor'},
                 {'name': 'Fire Staff', 'power': 86, 'type': 'armor'}]

    mages = [{'name': 'Jordan', 'power': 70, 'element': 'water'},
             {'name': 'Jordan', 'power': 93, 'element': 'ice'},
             {'name': 'Riley', 'power': 56, 'element': 'shadow'},
             {'name': 'Casey', 'power': 74, 'element': 'ice'},
             {'name': 'Riley', 'power': 55, 'element': 'lightning'}]

    spells = ['tornado', 'meteor', 'fireball', 'earthquake']
    print("Testing artifact sorter...")

    print(artifact_sorter(artifacts))
    print()
    print(power_filter(mages, 10))
    print()
    print(spell_transformer(spells))
