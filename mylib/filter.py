def filter(operations: list) -> list:
    acc = {}
    for o in operations:
        stored = acc.get(o["id"])
        if stored == None or stored["timestamp"] < o["timestamp"]:
            acc[o["id"]] = o
    return list(acc.values())
