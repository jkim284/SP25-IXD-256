## Introduction   

This project is a toy donation box dedicated specifically for toy donatoins for children. I first thought of this idea becasue of a project for another class- we had been researching about the recent LA fires and the aftermath of it. Becasue of this, I had originally thought of this as a donation box for
people who have been affected by natural disasters, but I realized that there were already similar products, and decided to focus on something for the children who could have also been affected by natiral disasters as well. If it's hard on adults, it would be an unimaginable experience for kids, and I
wanted to think of a way that could help them to find even a little comfort during the trying times.

## Implementation   

The box consists of two sensors, a screen, and a LED light strip all placed within a wooden box, where the donation will also go. It is designed so that the hardware all rests inside the box, and is covered by various compartments inside the box. The Box it's self is divded into five parts- two parts for the lid, and three parts for the actual box. The LED strip, phone screen, and light sensor is placed on the lid while the proximity sensor and ATOM Matrix is placed in a hollow section inside the box. The box itself was created by laser cutting multiple layers of the same teddy bear shape, and gluing them together. It was then sanded and prepped to actually store and house the hardware components.

### State Diagram
  
![Flow Chart](https://github.com/user-attachments/assets/72b7edd0-fa0c-4f30-979b-11549e992fd7)

### Hardware

* LED light  - Gives the donor feedback about the box
* Light Sensor  - Senses when the lid has been lifted
* Proximity Sensor  - Senses when a toy has been placed into the box

![IMG_4695](https://github.com/user-attachments/assets/062d950e-61a2-4a9c-87c1-f78c726f0a80)
  
### Schematic or Wiring Diagram

<img width="982" alt="Screenshot 2025-04-25 at 16 18 23" src="https://github.com/user-attachments/assets/41c73a1a-073a-4501-9965-66147c12685a" />

### Firmware   

``` Python  
from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep, sleep_ms

# --- Hardware setup ---

# Light sensor on pin 1
light_adc = ADC(Pin(1, Pin.IN))
light_adc.atten(ADC.ATTN_11DB)

# IR sensor on pin 7
IR_adc = ADC(Pin(7, Pin.IN))
IR_adc.atten(ADC.ATTN_11DB)

# NeoPixel strip on pin 38, with 15 LEDs
NUM_PIXELS = 7
np = NeoPixel(Pin(38, Pin.OUT), NUM_PIXELS)

# --- Thresholds (calibrate these!) ---
LIGHT_THRESHOLD = 4000    # adjust so light_val > this → “light triggered”
IR_THRESHOLD    = 300    # adjust so IR_val   > this → “IR triggered”

# --- Helpers ---

def set_all(r, g, b):
    for i in range(NUM_PIXELS):
        np[i] = (r, g, b)
    np.write()

# State 1 animation: one pixel every 3 s until full, then clear, repeat
def state_one_animation():
        for i in range(7):
                #set_all(0, 0, 0)
                sleep_ms(1000)
                np[i] = (255, 255, 255)
                
                np.write()
                # 3 s in 30 × 100 ms chunks so we can re‑check sensors
        set_all(0,0,0)
        for i in range(7):
            sleep_ms(1000)
            lv = light_adc.read()
            iv = IR_adc.read()
            if lv > LIGHT_THRESHOLD or iv < IR_THRESHOLD:
                return
                    
                # once full, clear and repeat
        

def state_two_light():
    for i in range(6):
        np[i] = (100, 100, 100)
        np.write()
        
def state_three_ir():
    for i in range(7):
        np[i] = (0, 100, 0)
        np.write()

# --- Main loop ---
while True:
    lv = light_adc.read()
    iv = IR_adc.read()
        #print('Main    | light_val =', lv, '| IR_val =', iv)
    print('light_val||' + str(lv))
    print('IR_val||' + str(iv))
    sleep_ms(100)
        
    if lv < LIGHT_THRESHOLD and iv > IR_THRESHOLD:
        state_two_light()
        print("OPEN")
    if iv < IR_THRESHOLD and lv < LIGHT_THRESHOLD:
        state_three_ir()
        print("REGISTERED")
    if lv > LIGHT_THRESHOLD and iv < IR_THRESHOLD:
        state_one_animation()
        print("IDLE")
```

### Software   

The main software I used was ProtoPie, and I wanted the users to interect with it- not just receive informaiton from it, so I had certain areas where the user had to input information regarding the toy directly into the screen.

### Integrations   

<img width="1711" alt="Screenshot 2025-04-25 at 15 05 44" src="https://github.com/user-attachments/assets/3bf68d5d-8fbc-44fe-9705-98287d5497ce" />

### Enclosure / Mechanical Design   

In order to cut my pieces, I first had to create an Illustrator file so that it could be brought in and cut in the Laser Lab.

<img width="1125" alt="Screenshot 2025-04-25 at 15 09 45" src="https://github.com/user-attachments/assets/7274248b-a16f-4b3f-a29d-5faacf567e02" />
<img width="1192" alt="Screenshot 2025-04-25 at 15 10 01" src="https://github.com/user-attachments/assets/812429c8-3fd7-48e1-ae66-3178d6610ff5" />
<img width="1146" alt="Screenshot 2025-04-25 at 15 10 17" src="https://github.com/user-attachments/assets/f27f1756-d32d-4a63-8bb2-64ca59abbe3a" />
<img width="1014" alt="Screenshot 2025-04-25 at 15 10 50" src="https://github.com/user-attachments/assets/ea8e6557-65d3-4dfe-8bc7-b4a43b90ec4a" />
<img width="953" alt="Screenshot 2025-04-25 at 15 11 24" src="https://github.com/user-attachments/assets/1292a145-e863-4b29-8218-c1cc8fcfd39c" />
<img width="833" alt="Screenshot 2025-04-25 at 15 10 28" src="https://github.com/user-attachments/assets/d3cdd644-269f-48ee-beb8-b218b1d4385f" />

Then I had to print it at the Laser Lab.


https://github.com/user-attachments/assets/f9b8b04f-f5f3-4eaf-a290-c38236dfa01b

![IMG_4260](https://github.com/user-attachments/assets/3b3a9774-b7a4-460f-b62e-6fba5562696d)

Afterwards, I had to glue it and sand it.
![IMG_4450](https://github.com/user-attachments/assets/c1d13c2f-a87b-42a1-aa4a-45eeef24acc7)
![IMG_4630](https://github.com/user-attachments/assets/19c07b79-07b4-4e01-a368-da47624c3e06)
![IMG_4640](https://github.com/user-attachments/assets/b7b66ea4-f591-4685-9510-f537c78dd1bb)


## Project outcome  

In the end, I got my prototype to work in the ways that I wanted it to, and I was satisfied with that- however, I think it can become somethign bigger and I would like to contiinue to work on it if a ever get a chance.  

https://drive.google.com/file/d/1XLTutUw4iPQv81phPq9Z0xN_yIiFFjMm/view?usp=sharing

## Conclusion  

All in all, I think I learned a lot about Protopie and using both software AND hardware both as means of making a product communicate and interact with the user. I think it was interesting to experiment with, and I hope to expand on this project further more in the future. 
