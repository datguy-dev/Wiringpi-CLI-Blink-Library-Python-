#### Having issues with wiringpi ports for Python? You may use this library to get the GPIO functioning and blinking an LED. If you can run gpio readall from CLI, then this will work. Currently, the script features solid and blinking LED states. All the colors supported by an RGB LED. The blink function is threaded and doesn't interrupt the code flow.

Adjust self.pins = [225,229,231] in rgbled.py to you desired BCM pins for the LED. Place rgbled.py in the same directory as the script you want to use it with and import it. Requires sh.

```
python3 -m pip install sh
```


```
#ex:

from rgbled import rgbled
from time import sleep

led = rgbled()
led.setup()

led.blink('white', 0.2) #this won't stop until....

for i in range(10):
  print('running other code....')
  sleep(1)

led.blink('off', 0) #here by turning off the led.
led.blink('red', 0.2) #or here starting another thread to blink.
sleep(3)
led.write('magenta') #this is not threaded
sleep(3)
led.write('off')

led.blink('off', 0) #the blink red wouldn't stop until here
```
