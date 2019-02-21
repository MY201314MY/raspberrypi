#!/usr/bin/python
import time
import subprocess
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
color = (0, 255, 0)
sense.low_light = True
print("pressing Up shows temperature; Down shows humidty;\nLeft shows pressure; Middle shows IP")
while True:
    for event in sense.stick.get_events():
        #print("The joystick was {} {} {}".format(event.action, event.direction, event.timestamp))
        if event.direction == 'up':
            if event.action == 'pressed':
                print("UP")
                print("pressed!")
                print ("Temperature: %s 'C" % round(sense.temp,2))
            elif event.action == 'released':
                print("UP")
                print("releaed")
                
        elif event.direction == 'down':
            if event.action == 'pressed':
                print("DOWN")
                print("pressed!")
                print ("Humity: %s R" % round(sense.humidity, 2))
            elif event.action == 'released':
                print("DOWN")
                print("releaed")

        elif event.direction == 'left':
            if event.action == 'pressed':
                print("Left")
                print("pressed!")
                pressure = 0
                while pressure == 0:
                    pressure = sense.get_pressure()
                print ("Pressure: %s Millibars" % round(pressure,2))

            elif event.action == 'released':
                print("Left")
                print("releaed")
                
        elif event.direction == 'right':
            if event.action == 'pressed':
                print("RIGHT")
                print("pressed!")
            elif event.action == 'released':
                print("RIGHT")
                print("releaed")
                
        elif event.direction == 'middle':
            if event.action == 'pressed':
                print("MIDDLE")
                print("pressed!")
                p = subprocess.Popen (["hostname","-I"],
                      stdout = subprocess.PIPE,
                      stderr = subprocess.PIPE)
                text = p.stdout.read().decode()
                error = p.stderr.read().decode()
                if len(error) > 0:
                    print("*****ERROR*****")
                    print(error)
    
                for line in text.splitlines():
                    print (line)
                    string = "IP:" + line
                    sense.show_message(string, scroll_speed = 0.1, text_colour=color)
                
            elif event.action == 'released':
                print("MIDDLE")
                print("releaed")
        else:
            time.sleep(0.020)