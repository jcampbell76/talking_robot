#!/usr/bin/env python3

from ev3dev2.sound import Sound

sound = Sound()

#there is spelled wrong, but this gets the right sound
pancake_lyrics_1 = 'Pancake robot, come and get them while there hot'
#say string with max volume (-a 200) and speed -s
opts = '-a 200 -s 200 '   
sound.speak(pancake_lyrics_1, espeak_opts=opts+'-ven')   

