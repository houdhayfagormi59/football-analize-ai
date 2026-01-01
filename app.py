from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
import cv2
import os

from core.detector import detect_players
from core.tracker import track_positions
from web.ui import homepage

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

positions = []

@app.get("/")
def home(request: Request):
    return homepage(request)

@app.post("/analyze")
async def analyze_video(video: UploadFile = File(...)):
    global positions
    positions = []

    path = "temp.mp4"
    with open(path, "wb") as f:
        f.write(await video.read())

    cap = cv2.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        players = detect_players(frame)
        track_positions(positions, players)

    cap.release()
    os.remove(path)

    return {
        "status": "analysis finished",
        "tracked_points": len(positions)
    }