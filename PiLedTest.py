import hal.hal_input_switch as switch
import hal.hal_led as led
import time
from time import sleep

def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
    # Initialize LED HAL driver 
    led.init()
    switch.init()
    start_time = time.time()
    end_time = start_time + 5

    while(True):
        if switch.read_slide_switch() == 0:
            while time.time()<end_time:
               blink_led(0.05)
            while switch.read_slide_switch()==0:
                start_time = time.time()
                end_time = start_time + 5
        else:
            blink_led(0.1)




    # Main entry point
if __name__ == "__main__":
    main()