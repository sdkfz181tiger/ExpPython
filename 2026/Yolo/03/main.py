# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2, os
from PIL import Image
from ultralytics import YOLO

def main():
    """ Main """
    print("main")

    # Model
    model = YOLO("yolo11n.pt")

    # Detection
    start_detection(model, "../assets/sample_01.mp4", "./out.mp4")


def start_detection(model, path_from, path_to):
    print("start_detection:", path_from, path_to)

    # Video(From)
    cap_from = cv2.VideoCapture(path_from)
    w     = int(cap_from.get(cv2.CAP_PROP_FRAME_WIDTH))# Width
    h     = int(cap_from.get(cv2.CAP_PROP_FRAME_HEIGHT))# Height
    count = int(cap_from.get(cv2.CAP_PROP_FRAME_COUNT))# Count
    fps   = int(cap_from.get(cv2.CAP_PROP_FPS))# Fps
    print("Video W:%d H:%d COUNT:%d FPS:%d" % (w, h, count, fps))

    # Video(To)
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    cap_to = cv2.VideoWriter(path_to, fourcc, fps, (w, h))

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break
        
        results = model(frame) # Prediction
        for result in results:
            # Draw Boxes
            xyxy = result.boxes.xyxy.cpu().numpy()
            for i in range(len(xyxy)):
                x1, y1, x2, y2 = xyxy[i]
                cv2.rectangle(frame,
                    pt1=(int(x1), int(y1)), 
                    pt2=(int(x2), int(y2)),
                    color=(33, 255, 33))
        drawGrid(w, h, frame, (33, 33, 33), 1)
        cap_to.write(frame)


def drawGrid(w, h, frame, l_color, l_width):
    g_size = int(w / 20)
    rows = int(h / g_size)
    cols = int(w / g_size)
    for r in range(1, rows):
        y = r * g_size
        cv2.line(frame, (0, y), (w, y), l_color, l_width)
        for c in range(1, cols):
            x = c * g_size
            cv2.line(frame, (x, 0), (x, h), l_color, l_width)


if __name__ == "__main__":
    main()