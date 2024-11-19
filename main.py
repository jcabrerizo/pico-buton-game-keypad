from display_control import SegmentDisplay
from game.game_control import GameControl
from machine import Pin
from time import sleep
import _thread

from board import BoardControl


board_led = Pin("LED", Pin.OUT)

board_control = BoardControl(board_led)
display_control = SegmentDisplay()
game_controls = GameControl(board_control, display_control)

# Start timer thread
timer_thread = _thread.start_new_thread(game_controls.timer, ())

while True:
    try:
        game_controls.evalute_preeses_loop()
        sleep(0.1)
    except KeyboardInterrupt:
        """ break loop with control + c """
        break

board_led.off()
print("Finished.")
