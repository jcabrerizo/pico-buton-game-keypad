from machine import Pin
from time import sleep
import random
import picokeypad
import _thread
import math


class Colours:
    red = (0xff, 0x00, 0x00)
    aquamarine = (0x00, 0xb4, 0x77)
    blue = (0x00, 0x00, 0xff)
    white = (0x00, 0x00, 0x00)


keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.1)
last_button_states = 0

timeout_time = 5

board_led = Pin("LED", Pin.OUT)
button_time_counter = 0
correct_pressed_buttons = -1
incorrect_pressed_buttons = 0
timeout_status = False
reset_request = False


def timeout_checker():
    global button_time_counter
    while True:
        if reset_request:
            board_led.toggle()
            sleep(0.2)
            board_led.toggle()
            sleep(0.2)
            board_led.high()
            sleep(0.2)
            reset_counters()
            print("New game")
        else:
            board_led.toggle()
            if correct_pressed_buttons == 0 and button_time_counter == 0:
                print("Starting game")
            if correct_pressed_buttons >= 0:
                button_time_counter += 1
            if button_time_counter > timeout_time:
                print(f"{correct_pressed_buttons} | {
                      incorrect_pressed_buttons} -> {correct_pressed_buttons * 100 / (correct_pressed_buttons + incorrect_pressed_buttons)}%")
                reset_counters()
            sleep(1)


def reset_counters():
    global correct_pressed_buttons, incorrect_pressed_buttons, button_time_counter, timeout_status, reset_request, target_button
    correct_pressed_buttons = -1  # first press is for starting
    incorrect_pressed_buttons = 0
    button_time_counter = 0
    timeout_status = False
    reset_request = False
    flash_all_leds()
    target_button = switch_random_led(target_button, Colours.aquamarine)


def flash_all_leds():
    for i in range(0, keypad.get_num_pads()):
        keypad.illuminate(i, 0x20, 0x00, 0x00)
    keypad.update()
    sleep(0.5)
    for i in range(0, keypad.get_num_pads()):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update()


def switch_random_led(old_led=None, colour=Colours.blue):
    if old_led is not None:
        keypad.illuminate(old_led, 0, 0, 0)
    new_led = random.randrange(0, 15)
    keypad.illuminate(new_led, colour[0], colour[1], colour[2])
    keypad.update()
    return new_led


def is_correct_press(button_states):
    global incorrect_pressed_buttons
    if int(math.log2(button_states)) == target_button:
        return True
    print(f"{hex(target_button)} != {
        hex(int(math.log2(button_states)))} ({button_states})")
    return False


target_button = None
reset_counters()

# Start timer thread
timer_thread = _thread.start_new_thread(timeout_checker, ())

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
                    target_button = switch_random_led(target_button)
                else:
                    incorrect_pressed_buttons += 1

        keypad.update()
        sleep(0.1)
    # break loop with control + c
    except KeyboardInterrupt:
        break

board_led.off()
print("Finished.")
