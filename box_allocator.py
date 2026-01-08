def assign_boxes(medicines):
    box_map = {}
    box_no = 1

    for med in medicines:
        box_map[med["name"]] = box_no
        box_no += 1

    return box_map
