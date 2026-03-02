def check_compliance(tracked_objects):
    persons = [obj for obj in tracked_objects if obj["label"] == "person"]
    helmets = [obj for obj in tracked_objects if obj["label"] == "helmet"]
    masks = [obj for obj in tracked_objects if obj["label"] == "mask"]

    violations = []

    for person in persons:
        px1, py1, px2, py2 = person["bbox"]
        pid = person["id"]

        helmet_found = any(
            hx1 < px2 and hx2 > px1 and hy1 < py2 and hy2 > py1
            for hx1, hy1, hx2, hy2 in [h["bbox"] for h in helmets]
        )

        mask_found = any(
            mx1 < px2 and mx2 > px1 and my1 < py2 and my2 > py1
            for mx1, my1, mx2, my2 in [m["bbox"] for m in masks]
        )

        if not helmet_found or not mask_found:
            violations.append((pid, person["bbox"]))

    return violations
