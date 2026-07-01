# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

import cv2, os
from PIL import Image
from ultralytics import YOLO, solutions

def main():
    """ Main """
    print("main")

    # Model
    # yolo11n < yolo11s < yolo11m ...
    # class:
    # 0: person, 2: car, 3: mortercycle,
    # 5: bus, 7: truck

    # Detection
    # start_detection(
    #     "yolo11n.pt", 
    #     path_from="../assets/sample_09.mp4", 
    #     path_to="./out_09.mp4",
    #     line_points=[(2900, 0), (2900, 2160)],
    #     classes=[0])
    
    start_detection(
        "yolo11n.pt", 
        path_from="../assets/sample_11.mp4", 
        path_to="./out_11.mp4",
        line_points=[(0, 800), (1080, 800)],
        classes=[2, 3, 5, 7])


def start_detection(path_model, path_from, path_to, line_points, classes):
    print("start_detection:", path_model, path_from, path_to)

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

    # Points
    counter = solutions.ObjectCounter(
        model=path_model, show=False, 
        region=line_points, classes=classes,
        line_width=4)

    # Render
    for n in range(count):
        ret, frame = cap_from.read()# Read
        if ret==False: break
        # Counter
        frame_counter = counter(frame)
        cap_to.write(frame_counter.plot_im)

    # Release
    cap_from.release()
    cap_to.release()
    cv2.destroyAllWindows()


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