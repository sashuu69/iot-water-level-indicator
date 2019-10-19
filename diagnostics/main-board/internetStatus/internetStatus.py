"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: internetStatus.py
 * Author : Sashwat K
 * Created on : 18 Oct 2019
 * Last updated : 18 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: Checking connection to firebase.google.com
"""
# Library to include socket functions
import socket

# URL to which the connection to be tested
REMOTE_SERVER = "firebase.google.com"


def is_connected(hostname):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


statusBool = is_connected(REMOTE_SERVER)
print(statusBool)
