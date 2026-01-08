def generate_alarms(medicines, box_map):
    alarms = []

    for med in medicines:
        for t in med["timings"]:
            alarms.append({
                "time": t,
                "tablet": med["name"],
                "box": box_map[med["name"]]
            })

    return alarms
