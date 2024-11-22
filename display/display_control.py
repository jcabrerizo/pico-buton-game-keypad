from machine import Pin
from .tm1637 import TM1637


class SegmentDisplay:
    def __init__(self, clk=Pin(26), dio=Pin(27)) -> None:
        self._display = TM1637(clk=clk, dio=dio)

    def time_and_score(self, remaining_time, points):
        self._display.numbers(num1=remaining_time, num2=points, colon=True)

    def scroll(self, msg, delay=250):
        self._display.scroll(msg, delay)

    def clear(self):
        self._display.show("    ")
