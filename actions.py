import unicornhat

def display_green():
    unicornhat.set_pixel(0, 0, 0, 255, 0)
    unicornhat.show()

def display_off():
    unicornhat.off()

def getSupportedActions():
    return {
        "green": display_green,
        "off": display_off
    }
