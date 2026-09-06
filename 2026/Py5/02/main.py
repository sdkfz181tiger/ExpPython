import time


def setup():
    py5.size(200, 200, py5.P2D)


def draw():
    if py5.frame_count % 50 == 0:
        py5.println(py5.frame_count)
    py5.square(py5.random_int(py5.width), py5.random_int(py5.height), 10)


py5.run_sketch(block=False)

print('start pause')
time.sleep(3)
print('end pause')