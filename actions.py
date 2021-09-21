import unicornhat, time
width, height = unicornhat.get_shape()

#-----------------------------------[ Colours ]-----------------------------------#
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN  = (0, 255, 0)
BLACK  = (0, 0, 0)

#----------------------------------[ Animations ]---------------------------------#
def raindrop(colour):
    for y in range(height):
        if (y % 2 == 0):
            for x in range(width):
                unicornhat.off()
                unicornhat.set_pixel(x, y, colour)
                unicornhat.show()
                time.sleep(0.075)
        else:
            for x in range(width):
                unicornhat.off()
                unicornhat.set_pixel(width-1 - x, y, colour)
                unicornhat.show()
                time.sleep(0.075)
    unicornhat.off()

def wipeUp(colour):
    for y in range(height):
        for x in range(width):
            unicornhat.set_pixel(x, height-1 - y, colour)
        unicornhat.show()
        time.sleep(0.1)

def wipeDown(colour):
    for y in range(height):
        for x in range(width):
            unicornhat.set_pixel(x, height-1 - y, colour)
        unicornhat.show()
        time.sleep(0.1)

#-----------------------------------[ Actions ]-----------------------------------#
def display_red():
    raindrop(RED)
    wipeUp(RED)

def display_yellow():
    raindrop(YELLOW)
    wipeUp(YELLOW)

def display_green():
    raindrop(GREEN)
    wipeUp(GREEN)

def display_off():
    wipeDown(BLACK)
    unicornhat.off()

#--------------------------------[ Action Lookup ]--------------------------------#

# Must be updated when new Actions are added so the main script can find them!
# Format is "action": display_actionname, lowercased names are required.
def getSupportedActions():
    return {
        "red": display_red,
        "yellow": display_yellow,
        "green": display_green,
        "off": display_off
    }
