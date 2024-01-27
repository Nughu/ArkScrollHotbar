import time

import pynput

# Variables
min_pos = 1  # define from which hotbar slot the scroll wheel should work
max_pos = 7  # define up to which hotbar slot the scroll wheel should work

# Main Process
pos = 1
controller = pynput.keyboard.Controller()
lastpos = 1


def on_scroll(x, y, dx, dy):
    direc = 'down' if dy < 0 else 'up'
    global pos
    global lastpos
    if direc == "down":
        if pos != min_pos:
            pos -= 1
        if pos != lastpos:
            controller.press((pynput.keyboard.KeyCode(pos + 48)))
            # time.sleep(0.25)
            controller.release((pynput.keyboard.KeyCode(pos + 48)))
    if direc == "up":
        if pos != max_pos:
            pos += 1
        if pos != lastpos:
            if pos == 10:
                controller.press(pynput.keyboard.KeyCode(48))
                # time.sleep(0.25)
                controller.release(pynput.keyboard.KeyCode(48))
            if pos != 10:
                controller.press((pynput.keyboard.KeyCode(pos + 48)))
                # time.sleep(0.25)
                controller.release((pynput.keyboard.KeyCode(pos + 48)))
    lastpos = pos


# ...or, in a non-blocking fashion:
listener = pynput.mouse.Listener(
    on_scroll=on_scroll)
listener.start()
input()