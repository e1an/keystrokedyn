import pyxhook
import time

def key_down(event):
    global running
    print(event.Key, " down")

    if event.Ascii == 13:
        running = False

def key_up(event):
    print(event.Key, " up")

hookman = pyxhook.HookManager()
#define callback to fire when key pressed down
hookman.KeyDown = key_down
hookman.KeyUp = key_up
hookman.HookKeyboard()
hookman.start()

running = True
while running:
    time.sleep(0.1)

hookman.cancel()