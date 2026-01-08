from datetime import time

TIME_MAP = {
    "Morning": time(8, 0),
    "Afternoon": time(13, 0),
    "Evening": time(18, 0),
    "Night": time(21, 0)
}

def normalize_time(time_text):
    return TIME_MAP.get(time_text, None)
import re

def parse_duration(duration_text):
    """
    '8 Days' -> 8
    """
    match = re.search(r"\d+", duration_text)
    return int(match.group()) if match else 1
