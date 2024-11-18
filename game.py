from machine import Pin
from time import sleep
import picokeypad
import _thread
import math

from leds import Colours, LedControl

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.1)
board_led = Pin("LED", Pin.OUT)
led_control = LedControl(board_led, keypad)

timeout_time = 5
last_button_states = 0
button_time_counter = 0
correct_pressed_buttons = -1
incorrect_pressed_buttons = 0
timeout_status = False
reset_request = False

def timer():
    global button_time_counter
    while True:
        if reset_request:
            reset_counters()
            print("New game")
        else:
            board_led.toggle()
            if correct_pressed_buttons == 0 and button_time_counter == 0:
                print("Starting game")
            if correct_pressed_buttons >= 0:
                button_time_counter += 1
            if button_time_counter > timeout_time:
                percentage = correct_pressed_buttons * 100 / \
                    (correct_pressed_buttons + incorrect_pressed_buttons) if (
                        correct_pressed_buttons + incorrect_pressed_buttons) > 0 else 0
                print(f"{correct_pressed_buttons} | {
                      incorrect_pressed_buttons} -> {percentage}%")
                reset_counters()
            sleep(1)


def reset_counters():
    global correct_pressed_buttons, incorrect_pressed_buttons, button_time_counter, timeout_status, reset_request, target_button
    correct_pressed_buttons = -1  # first press is for starting
    incorrect_pressed_buttons = 0
    button_time_counter = 0
    timeout_status = False
    reset_request = False
    led_control.flash_all_leds()
    target_button = led_control.switch_random_led(target_button, Colours.aquamarine)


def is_correct_press(button_states):
    correct_state = 2 ** target_button
    if button_states == correct_state:
        return True
    print(f"{hex(target_button)} != {
        hex(button_states)} ({button_states})")
    return False


target_button = None
reset_counters()

# Start timer thread
timer_thread = _thread.start_new_thread(timer, ())

while True:
    try:
        # Check for button pressed
        button_states = keypad.get_button_states()
        if last_button_states != button_states:
            last_button_states = button_states
            if button_states > 0:  # 0 means all buttons are released
                if button_states == 9:  # 1 and 4
                    reset_request = True
                    print("Reset requested")
                elif is_correct_press(button_states):
                    correct_pressed_buttons += 1
                    # turn on new button
                    target_button = led_control.switch_random_led(target_button)
                else:
                    incorrect_pressed_buttons += 1

        keypad.update()
        sleep(0.1)
    # break loop with control + c
    except KeyboardInterrupt:
        break

board_led.off()
print("Finished.")
