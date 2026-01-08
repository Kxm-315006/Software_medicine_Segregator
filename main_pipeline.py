import os
import json
from pathlib import Path

from ai.ner_extractor import extract_entities
from ai.medicine_logic import build_medicine_schedule
from ai.alarm_scheduler import build_alarm_schedule

PRESCRIPTION_DIR = "prescriptions"
OUTPUT_DIR = Path("output/alarms")


def save_alarm_output(prescription_name, alarms):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    out_file = OUTPUT_DIR / f"{prescription_name}.json"

    payload = {
        "prescription": prescription_name,
        "alarms": alarms
    }

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"📦 Alarm schedule saved → {out_file}")


def process_prescription(file_path):
    # 1. Read prescription
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 2. Run NER
    entities = extract_entities(text)

    # 3. Build structured medicine schedule
    structured = build_medicine_schedule(entities)

    # 4. Build alarm schedule
    alarms = build_alarm_schedule(structured)

    # 5. Print (software-level verification)
    print(f"\n📄 Prescription: {os.path.basename(file_path)}")
    for alarm in alarms:
        print(f"⏰ {alarm['datetime']} → {alarm['medicine']}")

    # 6. Persist output (CRITICAL FOR HARDWARE)
    save_alarm_output(Path(file_path).stem, alarms)

    return alarms


def run_pipeline():
    if not os.path.exists(PRESCRIPTION_DIR):
        print(f"❌ Folder '{PRESCRIPTION_DIR}' not found")
        return

    files = [f for f in os.listdir(PRESCRIPTION_DIR) if f.endswith(".txt")]

    if not files:
        print("❌ No prescription files found")
        return

    for file in files:
        file_path = os.path.join(PRESCRIPTION_DIR, file)
        process_prescription(file_path)
        print(f"✅ Processed {file}")


if __name__ == "__main__":
    run_pipeline()
