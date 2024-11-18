from game.game_control import GameControl
from machine import Pin
from time import sleep
import picokeypad # type: ignore
import _thread

from board import Colours, BoardControl

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.1)
board_led = Pin("LED", Pin.OUT)
board_control = BoardControl(board_led, keypad)

game_controls = GameControl(board_control)

# Start timer thread
timer_thread = _thread.start_new_thread(game_controls.timer, ())

while True:
    try:
        game_controls.evalute_preeses_loop()
        keypad.update()
        sleep(0.1)
    # break loop with control + c
    except KeyboardInterrupt:
        break

board_led.off()
print("Finished.")
