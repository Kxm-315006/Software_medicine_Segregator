from datetime import datetime, timedelta

DEFAULT_DURATION_DAYS = 7
DEFAULT_TIMES = {
    "Morning": "08:00",
    "Afternoon": "13:00",
    "Evening": "18:00",
    "Night": "21:00"
}

def parse_duration(text):
    try:
        return int(text.split()[0])
    except Exception:
        return DEFAULT_DURATION_DAYS


def normalize_times(times):
    if not times:
        return ["08:00"]

    result = []
    for t in times:
        result.append(DEFAULT_TIMES.get(t, "08:00"))
    return result


def build_alarm_schedule(structured_data):
    alarms = []

    for med in structured_data:
        # 🚨 HARD GUARD (THIS FIXES YOUR ERROR)
        if not isinstance(med, dict):
            continue

        name = med.get("medicine")
        if not name:
            continue

        durations = med.get("duration", [])
        times = med.get("time", [])

        days = parse_duration(durations[0]) if durations else DEFAULT_DURATION_DAYS
        time_slots = normalize_times(times)

        start_date = datetime.now().date()

        for day in range(days):
            for t in time_slots:
                alarms.append({
                    "medicine": name,
                    "date": str(start_date + timedelta(days=day)),
                    "time": t
                })

    return alarms
