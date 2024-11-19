from board.led_colours import Colours
from time import sleep

TIMEOUT_TIME = 5

class GameControl:
    def __init__(self, board_control) -> None:
        self.board_control = board_control
        self.last_button_states = 0
        self.target_button = None
        self.reset_counters()

    def timer(self):
        while True:
            if self.reset_request:
                self.reset_counters()
                print("New game")
            else:
                self.board_control.togle_led()
                if self.correct_pressed_buttons == 0 and self.button_time_counter == 0:
                    print("Starting game")
                if self.correct_pressed_buttons >= 0:
                    self.button_time_counter += 1
                if self.button_time_counter > TIMEOUT_TIME:
                    percentage = self.correct_pressed_buttons * 100 / \
                        (self.correct_pressed_buttons + self.incorrect_pressed_buttons) if (
                            self.correct_pressed_buttons + self.incorrect_pressed_buttons) > 0 else 0
                    print(f"{self.correct_pressed_buttons} | {
                        self.incorrect_pressed_buttons} -> {percentage}%")
                    self.reset_counters()
                sleep(1)

    def evalute_preeses_loop(self):
        button_states = self.board_control.get_button_states()
        if self.last_button_states != button_states:
            self.last_button_states = button_states
            if button_states > 0:  # 0 means all buttons are released
                if button_states == 9:  # 1 and 4
                    self.reset_request = True
                    print("Reset requested")
                elif self.is_correct_press(button_states):
                    self.correct_press()
                else:
                    self.incorrect_press()

    def reset_counters(self):
        self.correct_pressed_buttons = -1  # first press is for starting
        self.incorrect_pressed_buttons = 0
        self.button_time_counter = 0
        self.timeout_status = False
        self.reset_request = False
        self.board_control.flash_all_leds()
        self.target_button = self.board_control.switch_random_led(
            self.target_button, Colours.aquamarine)

    def is_correct_press(self, button_states):
        correct_state = 2 ** self.target_button
        if button_states == correct_state:
            return True
        print(f"{hex(self.target_button)} != {
            hex(button_states)} ({button_states})")
        return False

    def correct_press(self):
        self.correct_pressed_buttons +=1
        # turn on new button
        self.target_button = self.board_control.switch_random_led(
            self.target_button)
            
    def incorrect_press(self):
        self.incorrect_pressed_buttons +=1
        
