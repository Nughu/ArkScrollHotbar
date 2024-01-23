import time

import pynput

pos = 1
controller = pynput.keyboard.Controller()

# Main Process

def on_scroll(x, y, dx, dy):
    dir = 'down' if dy < 0 else 'up'
    global pos
    if dir == "down":
        if pos != 1:
            pos -= 1
        controller.press((pynput.keyboard.KeyCode(pos + 48)))
        #time.sleep(0.25)
        controller.release((pynput.keyboard.KeyCode(pos + 48)))
    if dir == "up":
        if pos != 10:
            pos += 1
        if pos == 10:
            controller.press(pynput.keyboard.KeyCode(48))
            #time.sleep(0.25)
            controller.release(pynput.keyboard.KeyCode(48))
        if pos != 10:
            controller.press((pynput.keyboard.KeyCode(pos + 48)))
            #time.sleep(0.25)
            controller.release((pynput.keyboard.KeyCode(pos + 48)))



# ...or, in a non-blocking fashion:
listener = pynput.mouse.Listener(
    on_scroll=on_scroll)
listener.start()
input()