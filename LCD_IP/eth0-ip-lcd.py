import socket
import fcntl
import struct
import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

dir=get_ip_address('eth0')  # '192.168.0.110'
mylcd.lcd_display_string("IP:%s " %dir, 1)
