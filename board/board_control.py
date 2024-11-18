from board.led_colours import Colours
from time import sleep
import random


class BoardControl:

    def __init__(self, led, keypad):
        self._led = led
        self._keypad = keypad

    def flash_all_leds(self):
        for i in range(0, self._keypad.get_num_pads()):
            self._keypad.illuminate(i, 0x20, 0x00, 0x00)
        self._keypad.update()
        for i in range(3):
            self._led.toggle()
            sleep(0.2)
        for i in range(0, self._keypad.get_num_pads()):
            self._keypad.illuminate(i, 0x00, 0x00, 0x00)
        self._keypad.update()

    def switch_random_led(self, old_led=None, colour=Colours.blue):
        if old_led is not None:
            self._keypad.illuminate(old_led, 0, 0, 0)
        new_led = random.randrange(0, 15)
        self._keypad.illuminate(new_led, colour[0], colour[1], colour[2])
        self._keypad.update()
        return new_led

    def togle_led(self):
        self._led.toggle()

    def get_button_states(self):
        return self._keypad.get_button_states()
