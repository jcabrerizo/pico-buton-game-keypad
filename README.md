# Buttons Game

This project is inspired by the Reaction Game at the [National Museum of Scotland](https://www.google.com/maps/@55.9470903,-3.1900278,2a,75y,219.26h,66.13t/data=!3m7!1e1!3m5!1s82RWNTWLpjnmGieTS4cLYA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D23.874962459582505%26panoid%3D82RWNTWLpjnmGieTS4cLYA%26yaw%3D219.25584788063242!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoJLDEwMjExMjMzSAFQAw%3D%3D).

## Hardware

This game is designed for the [Pimoroni RGB Keypad](https://shop.pimoroni.com/products/pico-rgb-keypad-base?variant=32369517166675).

Code examples are available in the official Pimoroni repository: <https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/pico_rgb_keypad>.

## How to Play

1. Press the `aquamarine` `#00B477` button to start a 5-second timer.  
2. During this period, press as many blue buttons as possible.  
3. When all the buttons turn red, the timer ends.

## Development Environment

- **IDE**: Visual Studio Code with the official [Raspberry Pi Pico extension](https://marketplace.visualstudio.com/items?itemName=raspberry-pi.raspberry-pi-pico).  
- **Setup**: Since the project consists of multiple files, the entire project must be uploaded to the device before running the `main.py` script.

## Planned Enhancements

1. **User Experience Improvements**  
   - [ ] Additional lighting effects.  
   - [ ] New game modes.  

2. **Display Integration**  
   - [x] Add a display to show the score: support a quad 7-segment LED display modules using the TM1637 LED driver using the [mcauser](https://github.com/mcauser/micropython-tm1637) library

3. **Customizable Game Duration**  
   - [ ] Allow players to adjust the game timer.  

4. **Multiplayer Features**  
   - [ ] Add Wi-Fi support for multiplayer modes.  
   - [ ] Implement score storage and leaderboards.  
