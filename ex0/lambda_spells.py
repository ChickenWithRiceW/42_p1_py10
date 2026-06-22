def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    res = {}
    res["max_power"] = max(key=lambda x: x["power"], *mages)
    res["min_power"] = min(key=lambda x: x["power"], *mages)
    res["avg_power"] = round(sum(i["power"] for i in mages), 2)

# if __name__ == "__main__":

    # Use the data_generator for this exercise to test it

    # print(artifact_sorter(artifacts))
    # print()
    # print(power_filter(mages, 10))
    # print()
    # print(spell_transformer(spells))
