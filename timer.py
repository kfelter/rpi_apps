#!/usr/bin/python
import sense_hat, time

MENU_STATE  = 0
TIMER_STATE = 1
FLASH_STATE = 2

sense = sense_hat.SenseHat()

sense.clear()

sense.show_message("set timer", text_colour = (255, 0, 0))
minutes = 20

def inc():
    global minutes
    minutes+=1

def dec():
    global minutes
    minutes-=1
    
def menu():
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                inc()

            if event.direction == "down":
                dec()

            if event.direction == "middle":
                return TIMER_STATE
    sense.show_message("{0}m".format(minutes))
    return MENU_STATE

def timer():
    while True:
        sense.clear()
        time.sleep(60*minutes)
        w = [255, 255, 255]
        sense.set_pixels([w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w,
                          w,w,w,w,w,w,w,w])
        time.sleep(5)
        sense.clear()
    return TIMER_STATE
     

# FSM
state = MENU_STATE
while True:
    if state == MENU_STATE:
        state = menu()
    elif state == TIMER_STATE:
        state = timer()
    else:
        exit
