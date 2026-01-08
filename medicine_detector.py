def detect_medicines(lines):
    medicines = []

    for line in lines:
        l = line.strip()
        low = l.lower()

        # Detect only medicine rows
        if not (
            low.startswith("tab")
            or low.startswith("cap")
            or low.startswith("1)")
            or low.startswith("2)")
            or low.startswith("3)")
            or low.startswith("4)")
        ):
            continue

        tokens = l.replace(",", "").split()

        name_parts = []
        timings = []
        days = None

        for i, t in enumerate(tokens):
            tl = t.lower()

            # Skip numbering
            if tl.endswith(")") and tl[:-1].isdigit():
                continue

            # Time detection
            if tl == "morning":
                timings.append("08:00")
                continue
            if tl == "night":
                timings.append("20:00")
                continue

            # Duration detection
            if tl == "days" and i > 0 and tokens[i - 1].isdigit():
                days = int(tokens[i - 1])
                continue

            # Skip keywords
            if tl in ["tab", "tab.", "cap", "cap.", "tablet", "capsule"]:
                continue

            if not tl.isdigit():
                name_parts.append(t)

        if name_parts:
            medicines.append({
                "name": " ".join(name_parts),
                "timings": sorted(set(timings)),
                "days": days
            })

    return medicines
