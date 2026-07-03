# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2, os
import utilities.utility as utility
from flask import Flask, render_template, Response
from moviepy import VideoFileClip, AudioFileClip, AudioArrayClip
from pathlib import Path
from PIL import Image
from ultralytics import YOLO, solutions

# Flask
app = Flask(__name__)

# WebCam
# Linux: $ ls /dev/video*
# Mac: $ system_profiler SPCameraDataType
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


def main():
    """ Main """
    print("main")

    # Server
    app.run(host="0.0.0.0", port=5000, debug=True)


def generate_frames():
    global w, h

    while True:
        # Camera
        success, frame = camera.read()
        if not success:
            break

        # Grid
        utility.draw_grid(w, h, frame, (255, 255, 255), 1)

        # Frame -> JPG
        ret, buffer = cv2.imencode(".jpg", frame)

        # JPG -> MIME
        yield(b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")


# Flask
@app.route("/")
def index():
    # Rendering
    return render_template("index.html")


@app.route("/video_streaming")
def video_streaming():
    # Streaming
    return Response(generate_frames(), 
        mimetype="multipart/x-mixed-replace; boundary=frame")



def start_prediction(path_file):
    print("start_prediction:", path_file)

    path = Path(path_file)
    path_from = path
    path_to   = path.name
    path_comp = Path(f"{path.stem}_comp{path.suffix}")
    
    # Video(From)
    cap_from   = cv2.VideoCapture(path_from)
    w          = int(cap_from.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
    h          = int(cap_from.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
    count      = int(cap_from.get(cv2.CAP_PROP_FRAME_COUNT))# Count
    fps        = int(cap_from.get(cv2.CAP_PROP_FPS))# Fps
    resolution = (w, h)
    print("Video W:%d H:%d COUNT:%d FPS:%d" % (w, h, count, fps))

    # Video(To)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    cap_to = cv2.VideoWriter(
        path_to, fourcc, fps, resolution)

    # Model
    model = YOLO("yolo26n.pt")

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break

        # Track
        frame_tracked = model.track(
            frame, persist=True, verbose=False)[0].plot()

        # Grid
        utility.draw_grid(w, h, frame_tracked, (255, 255, 255), 1)
        cap_to.write(frame_tracked)

    # Release
    cap_from.release()
    cap_to.release()
    
    # Audio
    #utility.write_audio(path_from, path_to, path_comp)


if __name__ == "__main__":
    main()