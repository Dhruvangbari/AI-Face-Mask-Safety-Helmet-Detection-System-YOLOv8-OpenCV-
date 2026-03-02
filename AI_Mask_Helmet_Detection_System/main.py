import cv2
from detector import detect
from tracker import SimpleTracker
from compliance import check_compliance
from logger import log_violation
from config import VIDEO_SOURCE

tracker = SimpleTracker()
cap = cv2.VideoCapture(VIDEO_SOURCE)

print("Industrial Safety Monitoring System Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)
    tracked = tracker.update(detections)
    violations = check_compliance(tracked)

    for obj in tracked:
        x1, y1, x2, y2 = obj["bbox"]
        color = (0,255,0)

        for pid, bbox in violations:
            if obj["id"] == pid:
                color = (0,0,255)
                log_violation(pid, frame)

        cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
        cv2.putText(frame, obj["label"], (x1, y1-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Industrial Safety Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
