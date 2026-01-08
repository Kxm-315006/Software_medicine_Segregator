import re
from datetime import datetime, timedelta

def extract_frequency(text):
    text = text.lower()

    # Common patterns
    match = re.search(r'(\d+)\s*(times?|x)\s*(a|per)?\s*day', text)
    if match:
        return int(match.group(1))

    if "once a day" in text or "1 time a day" in text:
        return 1
    if "twice a day" in text:
        return 2
    if "thrice a day" in text:
        return 3

    if "sos" in text:
        return 0  # SOS → manual trigger

    return 1  # default fallback


def generate_times(start="06:00", end="22:00", freq=1):
    if freq <= 1:
        return [start]

    fmt = "%H:%M"
    start_t = datetime.strptime(start, fmt)
    end_t = datetime.strptime(end, fmt)

    interval = (end_t - start_t) / freq
    times = []

    for i in range(freq):
        times.append((start_t + interval * i).strftime(fmt))

    return times
