import time
from selenium import webdriver


def weather(table):
    for n in table:
        url=n
        browser = webdriver.Firefox()
        browser.get(url=url)
        element = browser.find_element_by_id(id_="forecastID")
        message = element.text.split('℃\n')
        message[len(message)-1]=message[len(message)-1][0:len(message[len(message)-1])-1]

        low = {"city": "", "temperature": 100}
        high = {"city": "", "temperature": 0}
        for i in message:
            x, l = i.split('℃/')
            name, h = x.split('\n')
            if low['temperature'] > int(l):
                low['temperature'] = int(l)
                low['city'] = name
            if high['temperature'] < int(h):
                high['temperature'] = int(h)
                high['city'] = name
        print(high, low)
    browser.close()



url = ["http://www.weather.com.cn/html/province/sichuan.shtml","http://www.weather.com.cn/html/province/shandong.shtml","http://www.weather.com.cn/html/province/hubei.shtml"]
weather(url)