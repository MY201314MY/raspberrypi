import serial
from time import *


def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data


if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyUSB0', 9600)
    if serial.isOpen():
        print("open success")
    else:
        print("open failed")

    while True:
        s = bytes.fromhex('FDFDFD')
        serial.write(s)
        data = recv(serial)
        data = data.hex()
        if len(data) == 10:
            #print(data)
            if ord(data[2]) > 96:
                low = (ord(data[2])-87)*16
            else:
                low = (ord(data[2])-48)*16

            if ord(data[3]) > 96:
                low = low + ord(data[3])-87
            else:
                low = low + ord(data[3])-48

            if ord(data[4]) > 96:
                high = (ord(data[4])-87)*16
            else:
                high = (ord(data[4])-48)*16
            if ord(data[5]) > 96:
                high = high + ord(data[5])-87
            else:
                high = high + ord(data[5])-48
            sum = high*256 + low
            print("The high byte(高字节){0} and (低字节)low{1}".format(high, low))
            print("The result is:{0} (电导率)".format(sum))
            f = open("/home/pi/TFT/result.txt",'w')
            f.write(str(sum))
            f.close
        sleep(2)

