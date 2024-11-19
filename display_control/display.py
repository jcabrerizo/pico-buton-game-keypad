from machine import Pin
from .tm1637 import TM1637


class SegmentDisplay:
    def __init__(self, clk=Pin(26), dio=Pin(27)) -> None:
        self._mydisplay = TM1637(clk=clk, dio=dio)

    def time_and_score(self, remaining_time, points):
        self._mydisplay.numbers(num1=remaining_time, num2=points, colon=True)

    def clear(self):
        self._mydisplay.show("    ")
