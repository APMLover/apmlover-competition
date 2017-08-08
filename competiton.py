from dronekit import connect,VehicleMode
import time

import pygame

import sys


ttyUSB0 = '/dev/ttyUSB0'
ttyUSB1 = '/dev/ttyUSB1'
ttyUSB2 = '/dev/ttyUSB2'

PYJAltitude = 15

PythonScriptsLaunchingMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/com_boot.wav'
DeviceNumberMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/AssignedDeviceNumberIsCorrect.mp3'
SuccessfullyConnectedWithGroundVehicleMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/ship_suc_connect.wav'
TelemetryMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/telemet_connect.wav'
WaitingMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/Waiting_For_Command.mp3'
StartTrackingMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/start_tracking.wav'
TakingOffMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/oceaneye_TakesOff.wav'
GPSConditionMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/gps_good_cond.wav'
LandingMP3File = '/home/ubuntu/DroneChallenge/EnglishVoice/returns_home.wav'
pygame.mixer.pre_init(16000, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.init()


pygame.mixer.music.load(PythonScriptsLaunchingMP3File)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)


print "\nConnection Function Started, Connecting vehicle on : %s" % ttyUSB0

USB0Vehicle = connect(ttyUSB0, wait_ready = True, baud=57600)

print "\nConnection Function Complete"

print "\nttyUSB0's firmware : %s" % USB0Vehicle.version

if USB0Vehicle.version == "APM:Rover-3.1.2"  :
         print "Rover's DeviceNumber is Correct"    
    pygame.mixer.music.load(DeviceNumberMP3File)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

elif USB0Vehicle.version != "APM:Rover-3.1.2"  :
    print "Rover's DeviceNumber is unmatching"

Rover = USB0Vehicle

pygame.mixer.music.load(SuccessfullyConnectedWithGroundVehicleMP3File)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)


USB1Vehicle = connect(ttyUSB1, wait_ready = True, baud=57600)

print "USB1 Vehicle Version : %s" % USB1Vehicle.version

if USB1Vehicle.version == "APM:Copter-3.5.0-dev0" :
    print "Copter's Device Number is Correct"
    pygame.mixer.music.load(DeviceNumberMP3File)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)


elif USB1Vehicle.version != "APM:Copter-3.5.0-dev0" :
    print "Copter's Device Number is Unmatching"

MyCopter = USB1Vehicle


pygame.mixer.music.load(TelemetryMP3File)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)


while(1) :

    if MyCopter.mode.name == "GUIDED"  :           
        pygame.mixer.music.load(StartTrackingMP3File)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

        break


while(1) :

        if MyCopter.mode.name == "GUIDED" :

        dest = LocationGlobalRelative(Rover.location.global_frame.lat, Rover.location.global_frame.lon, PYJAltitude)
        MyCopter.simple_goto(dest)



        pygame.mixer.music.load(GPSConditionMP3File)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

        time.sleep(1)

    if MyCopter.mode.name != "GUIDED" :

        pygame.mixer.music.load(WaitingMP3File)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

        time.sleep(1)


print " \n completed "


pygame.mixer.music.load(LandingMP3File)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

sys.exit
