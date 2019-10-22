import pyxhook
import time

start_time = end_time = 0 #how tf do we calculate this
key_timing_array = []

def key_down(event):
    global running

    if event.Ascii == 13: #Return key pressed
        running = False

    print("Pressed ", event.Key, " down")
    print ("Measured time: ", time.time())

def key_up(event):
    print("Pressed ", event.Key, " up")

hookman = pyxhook.HookManager()
#define callback to fire when key pressed up/down
hookman.KeyDown = key_down
hookman.KeyUp = key_up
hookman.HookKeyboard()
hookman.start()

running = True
while running:
    time.sleep(0.1)

hookman.cancel()