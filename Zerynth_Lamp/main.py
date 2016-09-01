################################################################################
# Zerynth Lamp
#
# Created by Zerynth Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################



# import needed modules
import streams
from wireless import wifi
import animation
from toishield  import toishield
from bcm43362 import bcm43362  as wifi_driver


# and import the zerynthapp module
from zerynthapp import zerynthapp

streams.serial()

# connect to a wifi network
try:
    wifi_driver.auto_init()

    print("Establishing Link...")
    wifi.link("Zerynth",wifi.WIFI_WPA2,"zerynthwifi")

    print("Ok!")
        
except Exception as e:
    print(e)


# save the template.html in the board flash with new_resource
new_resource("template.html")

#### ZerynthApp Setup

# :: Javascript to Python ::
# the following functions will be called when buttons are pressed
def change_color(r, g, b):
    animation.setup_color(r, g, b)

def change_animation(n):
    animation.setup_anim(n)

def change_speed(n):
    animation.setup_anim_speed(n)

# configure the Zerynth app with a name, a descripton and the template url
vp = zerynthapp.ZerynthApp("Zerynth Lamp", "Try me!", "resource://template.html")

# everytime Javascript generates events the corresponding functions are called
vp.on("change_color", change_color)
vp.on("change_animation", change_animation)
vp.on("change_speed", change_speed)

# run the ZerynthApp!
vp.run()

# since vp.run starts a new thread, you can do whatever else you want down here!
# let's control leds

animation.start(D6, 24)