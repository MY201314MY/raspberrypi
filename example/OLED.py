import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
t=75
h=25

disp = Adafruit_SSD1306.SSD1306_128_64(rst=0)
disp.begin()
width = disp.width
height = disp.height
print(width)
print(height)
image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)
# Draw temperature / Humidity values.
draw.text((0, 8), '{0}°C'.format(t), fill=255)
draw.text((71, 8), '{0}%'.format(h), fill=255)
# Draw bar charts.
draw.rectangle((0, 0, 50, 8), outline=255, fill=0)
draw.rectangle((71, 0, 121, 8), outline=255, fill=0)
draw.rectangle((0, 0, t / 100.0 * 50, 8), outline=255, fill=255)
draw.rectangle((71, 0, 71 + (h / 100.0 * 50), 8), outline=255, fill=255)
# Send to OLED display.
disp.clear()
disp.image(image)
disp.display()
