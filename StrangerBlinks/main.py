################################################################################
# Stranger Blinks
#
# Created by Zerynth Team - 2016
# Author: Luigi F. Cerfeda
#
################################################################################

#### Import modules

# import modules for rtttl
from community.floyd.rtttl import rtttl

# import modules for neopixel
from neopixel import ledstrips as neo

# import the streams module, it is needed to send data around
import streams

# import modules for wifi connection and communication
from wireless import wifi
from bcm43362 import bcm43362 as wifi_driver
from zerynthapp import zerynthapp

# open the default serial port, the output will be visible in the serial console
s=streams.serial()

#### Define parameters and variables

# define a RTTTL melody to be played by passing it the RTTTL string.
# find more songs at http://ez4mobile.com/nokiatone/rtttf.htm and many other websites
#stranger_sounds = rtttl.tune("StrangerThings:d=4,o=5,b=170:8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8p,8c4,8e,8g,8b,8p,8g4,8b,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8p,8d4,8b,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8p,8d4,8b,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,p,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8p,8c4,8e,8g,8b,8p,8g4,8b,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8p,8d4,8b,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8p,8d4,8b,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,p,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8c,8e,8g,8b,8c6,8b,8g,8e,8e3,e.3,8e3,e.3,8e3,e.3,8e3,e.3,1e3")
stranger_sounds = rtttl.tune("StrangerThings:d=4,o=5,b=170:8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8c4,8p,8c4,8g,8b,8p,8c4,8p,8c4,8g,8e,8p,8p,8e4,8e,8g,8b,8p,8c4,8p,8c4,8g,8e,8p")


num_leds = 60                     # adjust this to match the number of LEDs on your strip
led_pin = D6                      # this should match the data pin of the LED strip

# define the letters printed on your wall and a set of colors
alphabet = "ABCDEFGHIYKLMNOPQRSTUVWXYZ"
colors = [(255,0,0), (0,255,0),(0,0,255),(255, 255, 0),(0,255,255), (255,0,255),(255,255,255)]

# associate letters to colors
alphabet_colors = {}
for i in alphabet:
    alphabet_colors[i] = colors[random(0, len(colors)-1)]

# positions = [i for i in range(num_leds)]

# alphabet_positions = {}
# for i,item in enumerate(alphabet):
#     alphabet_positions[item] = positions[i]

# hard coding to associate letters to positions
alphabet_positions = {'A':0, 'B':2, 'C':4, 'D':6, 'E':8, 'F':10, 'G':12, 'H':14,
                       'I':36, 'J':34, 'K':32, 'L':30, 'M':29, 'N':27, 'O':25, 'P':23, 'Q':21,
                       'R': 41, 'S':43, 'T':45, 'U':47, 'V':49, 'W': 51, 'X':53, 'Y': 55, 'Z':57}

# define the default message to be blinked and set sound to off
running_message = ""
sound_enabled = 0

# create a new Neopixel strip composed of <num_leds> LEDs and connected to pin led_pin
leds = neo.LedStrip(led_pin, num_leds) 

# set how long leds are on and off
time_on=1250
time_off=500

# associate colors to letter through positions and blink the leds
for i in alphabet:
    leds[alphabet_positions[i]] = alphabet_colors[i]
leds.on()

# save the template.html in the board flash with new_resource
new_resource("template.html")


#### WIFI CONNECTION

# init the wifi driver!
# The driver automatically registers itself to the wifi interface
# with the correct configuration for the selected board
wifi_driver.auto_init()

# use the wifi interface to link to the Access Point
# change network name, security and password as needed
# connect to a wifi network
for i in range(3):
    try:
        print("Establishing Link...")
        wifi.link("Zerynth",wifi.WIFI_WPA2,"zerynthwifi")
        print("Ok!")
        break # cool, we are connected
    except Exception as e:
        print(e)
        continue  # try again
else:
    print("Failed") # sorry can't connect

#### Define the functions

def clean_message(msg):
    msg = msg.upper()
    for i in msg:
        if i not in alphabet and i != ' ': # blank spaces are allowed
            clean_msg = msg.replace(i,'')
            msg = clean_msg
    return msg

def random_blink():
    leds.setall(random(0,255),random(0,255),random(0,255))
    leds.on()
    sleep(time_on)
    leds.clear()
    leds.on()
    

# To be continuously executed by a thread a function requires an infinite loop

def play_sound():
    global sound_enabled
    while True:
        if sound_enabled:
            print("Start Melody")
            print("-"*30)
            print("STRANGER THINGS")
            print("-"*30)
            # play the melody actuating the PWM of pin D2
            stranger_sounds.play(D2.PWM)
            print("Finished")
            print()

def blink_message():
    global running_message
    running_message = clean_message(running_message)
    while True:
        leds.clear()
        leds.on()
        sleep(time_off)
        for i in running_message:
            if i == ' ':
                leds.clear()
                leds.on()
                sleep(time_on)
                leds.clear()
                leds.on()
                sleep(time_off)
            else:
                leds[alphabet_positions[i]]=alphabet_colors[i]
                leds.on()
                sleep(time_on)
                leds.clear()
                leds.on()
                sleep(time_off)
        random_blink()


#### ZerynthApp Setup

# the following functions will be called when the buttons on the Zerynth App are pressed
def change_message(message):
    global running_message
    running_message = message
    running_message = clean_message(running_message)

def enable_sound(flipswitch_status):
    global sound_enabled
    if flipswitch_status == 'on':
        sound_enabled = 1
        print(flipswitch_status)
        print(sound_enabled)
    elif flipswitch_status == 'off':
        sound_enabled = 0
        print(flipswitch_status)
        print(sound_enabled)

# configure the zerynth app with a name, a descripton and the template url
zp = zerynthapp.ZerynthApp("Stranger Blinks","Messages from the Upside Down","resource://template.html")

# everytime Javascript generates the event "change_message" the function change_message is called
zp.on("change_message",change_message)

# everytime Javascript generates the event "enable_sound" the function enable_sound is called
zp.on("enable_sound", enable_sound)

# run the ZerynthApp!
zp.run()

# since zp.run starts a new thread, you can do whatever else you want down here!

# define the threads that allow to blink the message and play the sound
thread(play_sound)
thread(blink_message)
