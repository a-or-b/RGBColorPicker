"""
    Project: RGB Color Picker
    File: rgbcolorpicker.py
    Author: Akuma Ukpo
    Date: 7/11/23
    Description: RP2040 Web Server with RGB controls
"""

import network
import socket
import machine
import neopixel
import plasma
from plasma import plasma_stick

# Set how many LEDs you have
NUM_LEDS = 50

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# Start updating the LED strip
led_strip.start()

# Connect to Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<SSID>', '<PASSWORD>')
while not sta_if.isconnected():
    pass

# Print the IP address
print('IP address:', sta_if.ifconfig()[0])

# Set up the web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def set_hue_brightness(hue, brightness):
    for i in range(NUM_LEDS):
        led_strip.set_hsv(i, hue, 1.0, brightness)

# Handle incoming requests
while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)

    # Parse the request to get the hue and brightness values
    h_start = request.find('/?h=') + 4
    h_end = request.find('&', h_start)
    b_start = request.find('&b=') + 3
    b_end = request.find(' ', b_start)

    if h_start != -1 and b_start != -1:
        try:
            h = float(request[h_start:h_end])
            b = float(request[b_start:b_end])
            set_hue_brightness(h, b)
        except ValueError:
            pass

    # Send the response
    response = """<!DOCTYPE html>
<html>
<head>
<title>RGB Color Picker</title>
<style>
body {
  text-align: center;
}
.palette {
  width: 300px;
  height: 100px;
  background: linear-gradient(to right, red, yellow, lime, cyan, blue, magenta, red);
  margin: auto;
}
</style>
</head>
<body>
<h1>RGB Color Picker</h1>
<div class="palette" onclick="submitForm(event)"></div>
<br>
<label for="brightness">Brightness:</label>
<input type="range" min="0" max="1" step="0.01" value="1" id="brightness" onchange="submitForm()">
<br>
<script>
function submitForm(event) {
  var hue;
  if (event) {
    var rect = event.target.getBoundingClientRect();
    var x = event.clientX - rect.left;
    hue = x / rect.width;
  } else {
    hue = document.getElementById("hue").value;
  }
  var brightness = document.getElementById("brightness").value;
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/?h="+hue+"&b="+brightness, true);
  xhr.send();
}
</script>
</body>
</html>"""
    conn.send(response)
    conn.close()
