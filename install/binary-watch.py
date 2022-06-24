#!/usr/bin/env python

from locale import MON_5
import sys
from datetime import datetime
import signal
import time
import random
from signal import pause
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED


class Button_Handler:
    last_pushed_direction = "up"


def exit_handler(signum, frame):
    sense = SenseHat()
    sense.show_message("Programmet slutter")
    sense.clear()
    exit(1)

 
 
signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler) # Kill command

def get_default_binary_length(integer_in_clock, length):
    binary_representation = str(bin(int(integer_in_clock)))[2:]

    while length > len(binary_representation):
        binary_representation = "0" + binary_representation
    
    return binary_representation


def model1():
    sense = SenseHat()
    sense.low_light = True

    VIOLET_LIGHT    = [207, 159, 255]
    RED             = [255, 0, 0]
    GREEN           = [0, 255, 0]
    BLUE            = [0, 0, 255]
    PURPLE          = [255, 165, 0]
    NO_LIGHT        = [0,0,0]

    BACKGROUNDCOLOR = VIOLET_LIGHT
    
    JOYSTIK = PURPLE

    J = JOYSTIK
    B = BACKGROUNDCOLOR
    O = NO_LIGHT



    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    
    for number in range (0, len(current_time)):
        binary_representation = get_default_binary_length(current_time[number], 4)

        HOUR_UPPER = 0
        HOUR_LOWER = 1

        MINUTE_UPPER = 2
        MINUTE_LOWER = 3

        SECONDS_UPPER = 4
        SECONDS_LOWER = 5

        if (HOUR_UPPER == number):
                h1_2 = BLUE if "1" == binary_representation[2] else BACKGROUNDCOLOR
                h1_1 = BLUE if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (HOUR_LOWER == number):
                h2_4 = BLUE if "1" == binary_representation[0] else BACKGROUNDCOLOR
                h2_3 = BLUE if "1" == binary_representation[1] else BACKGROUNDCOLOR
                h2_2 = BLUE if "1" == binary_representation[2] else BACKGROUNDCOLOR
                h2_1 = BLUE if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (MINUTE_UPPER == number):
                m1_3 = GREEN if "1" == binary_representation[1] else BACKGROUNDCOLOR
                m1_2 = GREEN if "1" == binary_representation[2] else BACKGROUNDCOLOR
                m1_1 = GREEN if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (MINUTE_LOWER == number):
                m2_4 = GREEN if "1" == binary_representation[0] else BACKGROUNDCOLOR
                m2_3 = GREEN if "1" == binary_representation[1] else BACKGROUNDCOLOR
                m2_2 = GREEN if "1" == binary_representation[2] else BACKGROUNDCOLOR
                m2_1 = GREEN if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (SECONDS_UPPER == number):
                s1_3 = RED if "1" == binary_representation[1] else BACKGROUNDCOLOR
                s1_2 = RED if "1" == binary_representation[2] else BACKGROUNDCOLOR
                s1_1 = RED if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (SECONDS_LOWER == number):
                s2_4 = RED if "1" == binary_representation[0] else BACKGROUNDCOLOR
                s2_3 = RED if "1" == binary_representation[1] else BACKGROUNDCOLOR
                s2_2 = RED if "1" == binary_representation[2] else BACKGROUNDCOLOR
                s2_1 = RED if "1" == binary_representation[3] else BACKGROUNDCOLOR

    binary_watch = [
        O,     J,     O,  O,     O,    O,  O,    O,
        B,     O,     B,  O,     O,    O,  O,    O,
        O,     B,     O,  O,     O,    O,  O,    O,
        O,     O,     O,  O,     O,    O,  O,    O,
        O,     h2_4,  O,  O,     m2_4, O,  O,    s2_4,
        O,     h2_3,  O,  m1_3,  m2_3, O,  s1_3, s2_3,
        h1_2,  h2_2,  O,  m1_2,  m2_2, O,  s1_2, s2_2,
        h1_1,  h2_1,  O,  m1_1,  m2_1, O,  s1_1, s2_1
    ] 

    sense.set_pixels(binary_watch)
    print(current_time)



def model2():
    sense = SenseHat()
    sense.low_light = True

    VIOLET_LIGHT    = [207, 159, 255]
    RED             = [255, 0, 0]
    GREEN           = [0, 255, 0]
    BLUE            = [0, 0, 255]
    PURPLE          = [255, 165, 0]
    NO_LIGHT        = [0,0,0]

    BACKGROUNDCOLOR = VIOLET_LIGHT
    
    JOYSTIK = PURPLE

    J = JOYSTIK
    B = BACKGROUNDCOLOR
    O = NO_LIGHT



    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    hours   = str(current_time[0:2])
    minutes = str(current_time[2:4])
    seconds = str(current_time[4:6])

    binary_hour =       get_default_binary_length(hours, 5)
    binary_minute =     get_default_binary_length(minutes, 6)
    binary_seconds =    get_default_binary_length(seconds, 6)
    

    h1 = BLUE if "1" == binary_hour[4] else BACKGROUNDCOLOR
    h2 = BLUE if "1" == binary_hour[3] else BACKGROUNDCOLOR
    h3 = BLUE if "1" == binary_hour[2] else BACKGROUNDCOLOR
    h4 = BLUE if "1" == binary_hour[1] else BACKGROUNDCOLOR
    h5 = BLUE if "1" == binary_hour[0] else BACKGROUNDCOLOR

    m1 = GREEN if "1" == binary_minute[5] else BACKGROUNDCOLOR
    m2 = GREEN if "1" == binary_minute[4] else BACKGROUNDCOLOR
    m3 = GREEN if "1" == binary_minute[3] else BACKGROUNDCOLOR
    m4 = GREEN if "1" == binary_minute[2] else BACKGROUNDCOLOR
    m5 = GREEN if "1" == binary_minute[1] else BACKGROUNDCOLOR
    m6 = GREEN if "1" == binary_minute[0] else BACKGROUNDCOLOR

    s1 = RED if "1" == binary_seconds[5] else BACKGROUNDCOLOR
    s2 = RED if "1" == binary_seconds[4] else BACKGROUNDCOLOR
    s3 = RED if "1" == binary_seconds[3] else BACKGROUNDCOLOR
    s4 = RED if "1" == binary_seconds[2] else BACKGROUNDCOLOR
    s5 = RED if "1" == binary_seconds[1] else BACKGROUNDCOLOR
    s6 = RED if "1" == binary_seconds[0] else BACKGROUNDCOLOR


    binary_watch = [
        O, B, O, O,  O,  O, O, O,
        B, O, J, O,  O,  O, O, O,
        O, B, O, O,  O, m6, O, s6,
        O, O, O, h5, O, m5, O, s5,
        O, O, O, h4, O, m4, O, s4,
        O, O, O, h3, O, m3, O, s3,
        O, O, O, h2, O, m2, O, s2,
        O, O, O, h1, O, m1, O, s1
    ] 

    sense.set_pixels(binary_watch)
    print(current_time)



def model3():
    sense = SenseHat()
    sense.low_light = True

    VIOLET_LIGHT    = [207, 159, 255]
    RED             = [255, 0, 0]
    GREEN           = [0, 255, 0]
    BLUE            = [0, 0, 255]
    PURPLE          = [255, 165, 0]
    NO_LIGHT        = [0,0,0]

    BACKGROUNDCOLOR = VIOLET_LIGHT
    
    JOYSTIK = PURPLE

    J = JOYSTIK
    B = BACKGROUNDCOLOR
    O = NO_LIGHT



    now = datetime.now()
    current_time = now.strftime("%I%M%S")
    hours   = str(current_time[0:2])
    minutes = str(current_time[2:4])
    seconds = str(current_time[4:6])

    binary_hour =       get_default_binary_length(hours, 5)
    binary_minute =     get_default_binary_length(minutes, 6)
    binary_seconds =    get_default_binary_length(seconds, 6)
    

    h1 = BLUE if "1" == binary_hour[4] else BACKGROUNDCOLOR
    h2 = BLUE if "1" == binary_hour[3] else BACKGROUNDCOLOR
    h3 = BLUE if "1" == binary_hour[2] else BACKGROUNDCOLOR
    h4 = BLUE if "1" == binary_hour[1] else BACKGROUNDCOLOR
    h5 = BLUE if "1" == binary_hour[0] else BACKGROUNDCOLOR

    m1 = GREEN if "1" == binary_minute[5] else BACKGROUNDCOLOR
    m2 = GREEN if "1" == binary_minute[4] else BACKGROUNDCOLOR
    m3 = GREEN if "1" == binary_minute[3] else BACKGROUNDCOLOR
    m4 = GREEN if "1" == binary_minute[2] else BACKGROUNDCOLOR
    m5 = GREEN if "1" == binary_minute[1] else BACKGROUNDCOLOR
    m6 = GREEN if "1" == binary_minute[0] else BACKGROUNDCOLOR

    s1 = RED if "1" == binary_seconds[5] else BACKGROUNDCOLOR
    s2 = RED if "1" == binary_seconds[4] else BACKGROUNDCOLOR
    s3 = RED if "1" == binary_seconds[3] else BACKGROUNDCOLOR
    s4 = RED if "1" == binary_seconds[2] else BACKGROUNDCOLOR
    s5 = RED if "1" == binary_seconds[1] else BACKGROUNDCOLOR
    s6 = RED if "1" == binary_seconds[0] else BACKGROUNDCOLOR


    binary_watch = [
        O, B, O, O,  O,  O, O, O,
        B, O, B, O,  O,  O, O, O,
        O, J, O, O,  O, m6, O, s6,
        O, O, O, h5, O, m5, O, s5,
        O, O, O, h4, O, m4, O, s4,
        O, O, O, h3, O, m3, O, s3,
        O, O, O, h2, O, m2, O, s2,
        O, O, O, h1, O, m1, O, s1
    ] 

    sense.set_pixels(binary_watch)
    print(current_time)


def model4():
    sense = SenseHat()
    sense.low_light = True

    VIOLET_LIGHT    = [207, 159, 255]
    RED             = [255, 0, 0]
    GREEN           = [0, 255, 0]
    BLUE            = [0, 0, 255]
    PURPLE          = [255, 165, 0]
    NO_LIGHT        = [0,0,0]

    BACKGROUNDCOLOR = VIOLET_LIGHT
    
    JOYSTIK = PURPLE

    J = JOYSTIK
    B = BACKGROUNDCOLOR
    O = NO_LIGHT



    now = datetime.now()
    current_time = now.strftime("%I%M%S")
    
    for number in range (0, len(current_time)):
        binary_representation = get_default_binary_length(current_time[number], 4)

        HOUR_UPPER = 0
        HOUR_LOWER = 1

        MINUTE_UPPER = 2
        MINUTE_LOWER = 3

        SECONDS_UPPER = 4
        SECONDS_LOWER = 5

        if (HOUR_UPPER == number):
                h1_2 = BLUE if "1" == binary_representation[2] else BACKGROUNDCOLOR
                h1_1 = BLUE if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (HOUR_LOWER == number):
                h2_4 = BLUE if "1" == binary_representation[0] else BACKGROUNDCOLOR
                h2_3 = BLUE if "1" == binary_representation[1] else BACKGROUNDCOLOR
                h2_2 = BLUE if "1" == binary_representation[2] else BACKGROUNDCOLOR
                h2_1 = BLUE if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (MINUTE_UPPER == number):
                m1_3 = GREEN if "1" == binary_representation[1] else BACKGROUNDCOLOR
                m1_2 = GREEN if "1" == binary_representation[2] else BACKGROUNDCOLOR
                m1_1 = GREEN if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (MINUTE_LOWER == number):
                m2_4 = GREEN if "1" == binary_representation[0] else BACKGROUNDCOLOR
                m2_3 = GREEN if "1" == binary_representation[1] else BACKGROUNDCOLOR
                m2_2 = GREEN if "1" == binary_representation[2] else BACKGROUNDCOLOR
                m2_1 = GREEN if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (SECONDS_UPPER == number):
                s1_3 = RED if "1" == binary_representation[1] else BACKGROUNDCOLOR
                s1_2 = RED if "1" == binary_representation[2] else BACKGROUNDCOLOR
                s1_1 = RED if "1" == binary_representation[3] else BACKGROUNDCOLOR
        elif (SECONDS_LOWER == number):
                s2_4 = RED if "1" == binary_representation[0] else BACKGROUNDCOLOR
                s2_3 = RED if "1" == binary_representation[1] else BACKGROUNDCOLOR
                s2_2 = RED if "1" == binary_representation[2] else BACKGROUNDCOLOR
                s2_1 = RED if "1" == binary_representation[3] else BACKGROUNDCOLOR

    binary_watch = [
        O,     B,     O,  O,     O,    O,  O,    O,
        J,     O,     B,  O,     O,    O,  O,    O,
        O,     B,     O,  O,     O,    O,  O,    O,
        O,     O,     O,  O,     O,    O,  O,    O,
        O,     h2_4,  O,  O,     m2_4, O,  O,    s2_4,
        O,     h2_3,  O,  m1_3,  m2_3, O,  s1_3, s2_3,
        h1_2,  h2_2,  O,  m1_2,  m2_2, O,  s1_2, s2_2,
        h1_1,  h2_1,  O,  m1_1,  m2_1, O,  s1_1, s2_1
    ] 

    sense.set_pixels(binary_watch)
    print(current_time)


def any(event):
    if event.action != ACTION_RELEASED:
        Button_Handler.last_pushed_direction = event.direction
        sense = SenseHat()
        sense.clear()
    


def main():
    sense = SenseHat()
    sense.show_message("Programmet starter")
    sense.stick.direction_any   = any

    while True:
        if Button_Handler.last_pushed_direction == 'up':
            model1()
        elif Button_Handler.last_pushed_direction == 'right':
            model2()
        elif Button_Handler.last_pushed_direction == 'down':
            model3()
        elif Button_Handler.last_pushed_direction == 'left':
            model4()

if __name__ == '__main__':
    main()
