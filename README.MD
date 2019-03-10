# H1 Having issues with wiringpi ports for Python? You may use this library to get the GPIO functioning and blinking an LED. If you can run gpio readall from CLI, then this will work. 

# H4 Currently, the script features solid and blinking LED states. All the colors supported by an RGB LED. The blink function is threaded and doesn't interrupt the code flow.

Adjust self.pins = [225,229,231] in rgbled.py to you desired BCM pins for the LED.

```
from rgbled import rgbled
from time import sleep

led = rgbled()
led.setup()

led.blink('white', 0.2)
sleep(3)
led.blink('off', 0)
sleep(3)
led.blink('red', 0.2)
sleep(3)
led.write('magenta')
sleep(3)

led.blink('off', 0)
led.write('off')
```
