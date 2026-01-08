from ocr.prescription_reader import read_prescription
from logic.medicine_detector import detect_medicines
from logic.box_allocator import assign_boxes
from logic.alarm_generator import generate_alarms

IMAGE_PATH = "data/prescription.jpg"

print("✅ SYSTEM INITIALIZED")

lines = read_prescription(IMAGE_PATH)

medicines = detect_medicines(lines)
boxes = assign_boxes(medicines)
alarms = generate_alarms(medicines, boxes)

print("\n📦 MEDICINES DETECTED:")
for m in medicines:
    print("-", m)

print("\n📥 BOX ASSIGNMENT:")
for k, v in boxes.items():
    print(f"{k} → Box {v}")

print("\n⏰ ALARMS:")
for a in alarms:
    print(f"{a['time']} → Box {a['box']} ({a['tablet']})")
