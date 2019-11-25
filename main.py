#!/usr/bin/env python3

from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from threading import Thread
from time import sleep

def voice():
    sound = Sound()
    pancake_lyrics_1 = 'Pancake robot'
    pancake_lyrics_2 = 'come and get them while there hot'
    opts = '-a 200 -s 100 '
    sound.speak(pancake_lyrics_1, espeak_opts=opts+'-ven')   
    opts = '-a 200 -s 200 '
    sound.speak(pancake_lyrics_2, espeak_opts=opts+'-ven')

def beat():
    sound = Sound()
    # Play a 500 Hz tone for 1 second and then wait 0.4 seconds
    # before playing the next tone 
    # Play the tone three times
    sound.tone([(200, 2000, 400),(800, 1000, 3000)])
    #sound.tone(2000, 1500).wait()
    #sleep(1)
    #sound.tone(1000, 1500).wait()
    #sound.tone([(3000, 2000, 400),(800, 1800, 2000)]).wait()
    #sound.tone([(1000, 1000, 400)] * 3).wait()


t_voice = Thread(target=voice)
t_voice.start()
#t_beat = Thread(target=beat)
#t_beat.start()

leds = Leds()



leds.all_off() # Turn all LEDs off
sleep(1)

#there is spelled wrong, but this gets the right sound
pancake_lyrics_1 = 'Pancake robot'
pancake_lyrics_2 = 'come and get them while there hot'
opts = '-a 200 -s 100 '

# Set both pairs of LEDs to amber
leds.set_color('LEFT', 'RED')
leds.set_color('RIGHT', 'GREEN')
sleep(1)
#say string with max volume (-a 200) and speed -s   

# Set both pairs of LEDs to amber
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'RED')
sleep(1)
#sound.speak('Robot', espeak_opts=opts+'-ven')   

# With custom colors:
leds.set_color('LEFT', (1, 0)) # Bright Red.
leds.set_color('RIGHT', (0, 1)) # Bright green.
sleep(4)



