# RGB Color Picker

## Overview
This project is a web server that runs on an RP2040 and allows users to control the hue and brightness of an RGB LED strip. The web server serves a simple HTML page with a color palette and a brightness slider that users can interact with to change the color of the LED strip.

## Requirements
- RP2040 microcontroller
- WS2812 / NeoPixel™ LED strip with 50 LEDs
- Plasma library for Python

## Usage
1. Update the `<SSID>` and `<PASSWORD>` placeholders in the code with your Wi-Fi network credentials.
2. Connect the LED strip to the RP2040 according to the pin assignments in the code.
3. Run the `rgbcolorpicker.py` script on the RP2040.
4. Once the script is running, it will connect to the specified Wi-Fi network and print its IP address.
5. Open a web browser and navigate to the IP address of the RP2040 to access the RGB Color Picker web page.
6. Use the color palette and brightness slider on the web page to control the hue and brightness of the LED strip.

## Author
Akuma Ukpo

## Date
7/11/23
