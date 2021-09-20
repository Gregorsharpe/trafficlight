import unicornhat, time
width, height = unicornhat.get_shape()

#-----------------------------------[ Colours ]-----------------------------------#
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN  = (0, 255, 0)

#----------------------------------[ Animations ]---------------------------------#
def raindrop(colour):
    unicornhat.set_pixel(0, 0, colour)

def wipe(colour):
    for y in range(height):
        for x in range(width):
            unicornhat.set_pixel(x, y, colour)
        unicornhat.show()
        time.sleep(0.1)

        

#-----------------------------------[ Actions ]-----------------------------------#
def display_green():
    wipe(GREEN)

def display_off():
    unicornhat.off()

#--------------------------------[ Action Lookup ]--------------------------------#

# Must be updated when new Actions are added so the main script can find them!
# Format is "action": display_actionname, lowercased names are required.
def getSupportedActions():
    return {
        "green": display_green,
        "off": display_off
    }
