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
                unicornhat.set_pixel(x, y, colour)
                unicornhat.show()
                time.sleep(0.05)
        else:
            for x in range(width):
                unicornhat.set_pixel(x, y, colour)
                unicornhat.show()
                time.sleep(0.05)

def wipe(colour):
    for y in range(height):
        for x in range(width):
            unicornhat.set_pixel(x, y, colour)
        unicornhat.show()
        time.sleep(0.1)

        

#-----------------------------------[ Actions ]-----------------------------------#
def display_green():
    raindrop(GREEN)
    wipe(GREEN)

def display_off():
    wipe(BLACK)
    unicornhat.off()

#--------------------------------[ Action Lookup ]--------------------------------#

# Must be updated when new Actions are added so the main script can find them!
# Format is "action": display_actionname, lowercased names are required.
def getSupportedActions():
    return {
        "green": display_green,
        "off": display_off
    }
