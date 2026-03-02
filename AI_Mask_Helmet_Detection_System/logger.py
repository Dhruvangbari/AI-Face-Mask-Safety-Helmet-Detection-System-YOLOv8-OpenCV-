import os
import pandas as pd
import datetime
import time
from config import VIOLATION_COOLDOWN

os.makedirs("logs/images", exist_ok=True)

last_logged = {}

def log_violation(person_id, frame):
    current_time = time.time()

    if person_id in last_logged:
        if current_time - last_logged[person_id] < VIOLATION_COOLDOWN:
            return

    last_logged[person_id] = current_time

    timestamp = datetime.datetime.now()
    filename = f"logs/images/violation_{person_id}_{int(current_time)}.jpg"

    import cv2
    cv2.imwrite(filename, frame)

    df = pd.DataFrame([[timestamp, person_id]], columns=["timestamp", "person_id"])
    df.to_csv("logs/violations.csv", mode='a', header=not os.path.exists("logs/violations.csv"), index=False)
