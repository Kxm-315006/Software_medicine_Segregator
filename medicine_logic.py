def build_medicine_schedule(entities):
    """
    Input: entities -> list of dicts from NER
    Output: list of structured medicine dictionaries
    """

    medicines = []   # ✅ DEFINE IT

    current = None

    for ent in entities:
        label = ent.get("label")
        text = ent.get("text")

        if label == "MEDICINE":
            # start a new medicine entry
            current = {
                "medicine": text,
                "dosage": [],
                "time": [],
                "duration": []
            }
            medicines.append(current)

        elif current is not None:
            if label == "DOSAGE":
                current["dosage"].append(text)
            elif label == "TIME":
                current["time"].append(text)
            elif label == "DURATION":
                current["duration"].append(text)

    # ✅ FINAL SAFETY FILTER (VERY IMPORTANT)
    return [
        m for m in medicines
        if isinstance(m, dict) and m.get("medicine")
    ]
