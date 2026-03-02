import uuid

class SimpleTracker:
    def __init__(self):
        self.objects = {}

    def update(self, detections):
        tracked = []
        for det in detections:
            x1, y1, x2, y2, conf, label = det
            obj_id = str(uuid.uuid4())[:8]
            tracked.append({
                "id": obj_id,
                "bbox": (x1, y1, x2, y2),
                "label": label
            })
        return tracked
