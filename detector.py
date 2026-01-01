from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_players(frame):
    results = model(frame, verbose=False)
    players = []

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # person
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                players.append((cx, cy))

    return players