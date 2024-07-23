# Python code transmits a byte to Arduino /Microcontroller
import serial
import struct
import time
import math
from math import sqrt
import numpy


SerialObj = serial.Serial('COM12') # COMxx  format on Windows
                  # ttyUSBx format on Linux
SerialObj.baudrate = 112500  # set Baud rate to 9600
SerialObj.bytesize = 8   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1


def sendData(a,b,c):
    SerialObj.write(struct.pack('>BBB',a,b,c))

def receiveData():
    ReceivedString = SerialObj.readline()
    print(ReceivedString)

def convertCoordinate(x,y,z):  #Hàm chuyển từ hệ toạ độ descartes sang hệ toạ độ trụ
    armL1 = 100  #Độ dài cánh tay thứ 1 (đơn vị mm)
    armL2 = 100  #Độ dài cánh tay thứ 2 (đơn vị mm)
    corner1 = 0  #Góc quay của servo1
    corner2 = 0  #Góc quay của servo2
    # resolution = 1  #Độ phân giải (các điểm lấy mẫu cách nhau 1mm)
    
    c = sqrt(x**2+y**2)
    corner2 = math.degrees(numpy.arccos((armL1**2 + armL2**2 - c**2)/(2*armL1*armL2)))
    corner1 = math.degrees(numpy.arccos(x/c))+(180-corner2)/2

    # print(corner1,corner2)
    return corner1, corner2, z

def rectangle(w,h,x,y,z):
    resolution = 1 # Hằng lưu độ phân giải (độ chia nhỏ nhất hay khoảng cách giữa 2 điểm gần nhau nhất)
    DELAY = 0.05 # Hằng lưu khoảng delay giữa 2 lần gửi data qua serial
    for i in range(x, x+w, resolution):
        a,b,c = convertCoordinate(i,y,z)
        # print(round(a),round(b),round(c))
        time.sleep(DELAY)
        sendData(round(a),round(b),round(c))
        receiveData()
        # print(i,y,z)
    for i in range(y, y+h, resolution):
        a,b,c = convertCoordinate(x+w,i,z)
        # print(round(a),round(b),round(c))
        time.sleep(DELAY)
        sendData(round(a),round(b),round(c))
        receiveData()
        # print(x+w,i,z)
    for i in range(x+w, x, -resolution):
        a,b,c = convertCoordinate(i,y+h,z)
        # print(round(a),round(b),round(c))
        time.sleep(DELAY)
        sendData(round(a),round(b),round(c))
        receiveData()
        # print(i,y+h,z)
    for i in range(y+h, y-resolution, -resolution):
        a,b,c = convertCoordinate(x,i,z)
        # print(round(a),round(b),round(c))
        time.sleep(DELAY)
        sendData(round(a),round(b),round(c))
        receiveData()
        # print(x,i,z)

def printRectangle(w,h,x,y,z):
    resolution = 1 # Hằng lưu độ phân giải (độ chia nhỏ nhất hay khoảng cách giữa 2 điểm gần nhau nhất)
    DELAY = 0.05 # Hằng lưu khoảng delay giữa 2 lần gửi data qua serial
    for i in range(x, x+w, resolution):
        a,b,c = convertCoordinate(i,y,z)
        # print(round(a),round(b),round(c))
        print(a,b,c)
        # print(i,y,z)
    for i in range(y, y+h, resolution):
        a,b,c = convertCoordinate(x+w,i,z)
        # print(round(a),round(b),round(c))
        print(a,b,c)
        # print(x+w,i,z)
    for i in range(x+w, x, -resolution):
        a,b,c = convertCoordinate(i,y+h,z)
        # print(round(a),round(b),round(c))
        print(a,b,c)
        # print(i,y+h,z)
    for i in range(y+h, y-resolution, -resolution):
        a,b,c = convertCoordinate(x,i,z)
        # print(round(a),round(b),round(c))
        print(a,b,c)
        # print(x,i,z)

def circle(r,x0,y0,z):
    resolution = 1
    DELAY = 0.05
    for x in range(x0-r, x0+r+resolution, resolution):
        y = sqrt(r**2-(x-x0)**2)+y0
        a,b,c = convertCoordinate(x,y,z)
        # time.sleep(DELAY)
        # sendData(round(a),round(b),round(c))
        # receiveData()
        print(a,b,c)

    
    for x in range(x0+r, x0-r-resolution, -resolution):
        y = -sqrt(r**2-(x-x0)**2)+y0
        a,b,c = convertCoordinate(x,y,z)
        # time.sleep(DELAY)
        # sendData(round(a),round(b),round(c))
        # receiveData()
        print(a,b,c)


def perfectTriangle(a,x,y,z):
    resolution = 1




# a,b,c = convertCoordinate(10,10,0)

# print(a,b,c)


# time.sleep(0.05)
# sendData(45,45,0)
# receiveData()



# a,b,c = convertCoordinate(0, 150, 0)
# time.sleep(0.05)
# sendData(round(a),round(b),round(c))
# receiveData()

# resolution = 1 # Hằng lưu độ phân giải (độ chia nhỏ nhất hay khoảng cách giữa 2 điểm gần nhau nhất)
# DELAY = 0.01 # Hằng lưu khoảng delay giữa 2 lần gửi data qua serial
# y = 80
# h = 40
# x = 0
# z = 0
# for i in range(y, y+h, resolution):
#     a,b,c = convertCoordinate(x,i,z)
#     # print(round(a),round(b),round(c))
#     time.sleep(DELAY)
#     sendData(round(a),180-round(b),round(c))
#     receiveData()
#     # print(x+w,i,z)


rectangle(40,50,-20,80,0)

# circle(25, -20,100,0)

# time.sleep(3)
# sendData(65,66,67)
# receiveData()

SerialObj.close()      # Close the port

