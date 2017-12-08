from microbit import *

display.show(Image.HAPPY)
sleep(1500)

for img in CLOCK_IMAGES:
    display.show(img)
    sleep(1000)
