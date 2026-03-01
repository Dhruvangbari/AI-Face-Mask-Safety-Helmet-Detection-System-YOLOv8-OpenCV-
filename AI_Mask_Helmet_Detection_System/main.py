import cv2
import os
from detector import detect
from config import VIDEO_SOURCE, SAVE_VIOLATIONS
from utils import create_log, log_violation

create_log()
os.makedirs("logs/images", exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)

print("Industrial Safety Monitoring Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)

    persons = []
    helmets = []
    masks = []

    for obj in detections:
        label = obj["label"]
        x1, y1, x2, y2 = obj["bbox"]

        if label == "person":
            persons.append(obj)
        elif label == "helmet":
            helmets.append(obj)
        elif label == "mask":
            masks.append(obj)

    for person in persons:
        px1, py1, px2, py2 = person["bbox"]
        compliant = True

        # Check helmet overlap
        helmet_found = any(
            hx1 < px2 and hx2 > px1 and hy1 < py2 and hy2 > py1
            for hx1, hy1, hx2, hy2 in [h["bbox"] for h in helmets]
        )

        # Check mask overlap
        mask_found = any(
            mx1 < px2 and mx2 > px1 and my1 < py2 and my2 > py1
            for mx1, my1, mx2, my2 in [m["bbox"] for m in masks]
        )

        if not helmet_found or not mask_found:
            compliant = False

        color = (0,255,0) if compliant else (0,0,255)
        status = "SAFE" if compliant else "VIOLATION"

        cv2.rectangle(frame, (px1, py1), (px2, py2), color, 2)
        cv2.putText(frame, status, (px1, py1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        if not compliant and SAVE_VIOLATIONS:
            log_violation("Helmet/Mask Violation")
            filename = f"logs/images/violation_{int(cv2.getTickCount())}.jpg"
            cv2.imwrite(filename, frame)

    cv2.imshow("Industrial Safety Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
