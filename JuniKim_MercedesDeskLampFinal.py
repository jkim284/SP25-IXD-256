from machine import Pin, ADC
from time import sleep_ms, ticks_ms
from neopixel import NeoPixel
import math


# Configure pin 1 as input
analog_pin = Pin(1, Pin.IN)

# Configure ADC on input pin
adc = ADC(analog_pin)

# Configure the ADC sensitivity (11dB gives a larger voltage range)
adc.atten(ADC.ATTN_11DB)

# Configure touch input pin (assuming you'll connect copper pieces to pin 1)
touch_pin = Pin(1, Pin.IN, Pin.PULL_UP)  # Pull-up resistor to detect connection

# Create NeoPixel driver on pin 35 for 1 pixel (built-in RGB LED)
np = NeoPixel(Pin(35), 1)

# Create NeoPixel driver on pin 7 for 30 pixels (external LED strip)
np7 = NeoPixel(Pin(7), 30)

# Initialize variables
copper_separated = False
separation_time = 0
flash_state = False

# Function to set all LEDs to a specific color
def set_all_leds(color):
    # Set built-in LED
    np[0] = color
    np.write()
    
    # Set all LEDs in the strip
    for i in range(30):
        np7[i] = color
    np7.write()

# Turn off all LEDs initially
set_all_leds((0, 0, 0))

while True:
    # Read the touch pin (LOW/0 when copper pieces touch, HIGH/1 when separated)
    current_state = touch_pin.value()
   
    
    # Check if copper pieces are separated (HIGH/1)
    if current_state == 1:
        # If just separated, record the time
        if not copper_separated:
            copper_separated = True
            separation_time = ticks_ms()
            # Set LEDs to white immediately
            set_all_leds((255, 255, 255))
            
        # Calculate how long the copper pieces have been separated
        time_elapsed = ticks_ms() - separation_time
        
        # If more than 5 seconds (5000ms) have passed, start flashing
        if time_elapsed > 5000:
            # Toggle the flash state every 500ms
            if time_elapsed % 1000 < 500:
                if not flash_state:
                    set_all_leds((255, 255, 255))  # White
                    flash_state = True
            else:
                if flash_state:
                    pulse_intensity = int((math.sin(ticks_ms() / 1000) * 127 + 128))  # Sinusoidal pulse (slow and rhythmic)
                    for i in range(30):
                        np7[i] = (pulse_intensity, pulse_intensity, pulse_intensity)  # Soft white glow with pulse
                    np7.write()
    
    # If copper pieces are touching (LOW/0)
    else:
        # If just touched after being separated
        if copper_separated:
            copper_separated = False
            # Turn off all LEDs
            set_all_leds((0, 0, 0))
            flash_state = False
    
    # Small delay to prevent CPU overload
    sleep_ms(10)