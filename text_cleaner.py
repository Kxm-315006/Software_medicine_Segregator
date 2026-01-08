def clean_lines(text):
    lines = []
    for line in text.split("\n"):
        l = line.strip()
        if len(l) > 2:
            lines.append(l)
    return lines
