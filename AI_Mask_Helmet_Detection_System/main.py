import cv2
import os
import datetime
from detector import detect
from config import VIDEO_SOURCE

os.makedirs("logs", exist_ok=True)
os.makedirs("captures", exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)

print("AI Mask & Helmet Detection System Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)

    for (label, x1, y1, x2, y2) in detections:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{label}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        with open("logs/detection_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - {label} detected\n")

        filename = f"captures/detection_{int(datetime.datetime.now().timestamp())}.jpg"
        cv2.imwrite(filename, frame)

    cv2.imshow("AI Mask & Helmet Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
