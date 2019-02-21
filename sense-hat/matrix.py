#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.low_light = True
print (len(sense.get_pixels()))
sense.set_rotation(0)

color = (0, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
No = (0, 0, 0)
string = 'Network in the period!'
#sense.show_message(string, scroll_speed = 0.1, text_colour=color, back_colour = No)
sense.set_pixel (7, 6, 255, 0, 0)
print(sense.get_pixel (7,6))

print("The fllowing date comes from sense-hat:")
#Environmental sensors
print ("Humity: %s R" % round(sense.humidity, 2))
print ("Temperature: %s 'C" % round(sense.temp,2))

pressure = 0
while pressure == 0:
    pressure = sense.get_pressure()
print ("Pressure: %s Millibars" % round(pressure,2))