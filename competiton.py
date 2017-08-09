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

class Competiton():

    def __init__(self):
        self.rover = None
        self.copter = None

    def playmp3(self, filepath):
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

    def both_connected(self):
        ...

    def connect_rover(self):
        USB0Vehicle = connect(ttyUSB0, wait_ready = True, baud=57600)
        print "\nttyUSB0's firmware : %s" % USB0Vehicle.version
        if USB0Vehicle.version == "APM:Rover-3.1.2"  :
                 print "Rover's DeviceNumber is Correct"
            self.playmp3(DeviceNumberMP3File)
            self.rover = USB0Vehicle

        elif USB0Vehicle.version != "APM:Rover-3.1.2"  :
            print "Rover's DeviceNumber is unmatching"

    def connect_copter(self):

        USB1Vehicle = connect(ttyUSB1, wait_ready = True, baud=57600)

        print "USB1 Vehicle Version : %s" % USB1Vehicle.version

        if USB1Vehicle.version == "APM:Copter-3.5.0-dev0" :
            print "Copter's Device Number is Correct"
            self.playmp3(DeviceNumberMP3File)
            self.copter = USB1Vehicle

        elif USB1Vehicle.version != "APM:Copter-3.5.0-dev0" :
            print "Copter's Device Number is Unmatching"

    def connect_both(self):
        while True:
            if (self.rover is not None and
                self.copter is not None):
                return
            print("Waiting for vehicles....")
            time.sleep(1)

    def do_flight(self):
        self.playmp3(PythonScriptsLaunchingMP3File)

       while not self.both_connected():
           self.connect_both()

        Rover = USB0Vehicle

        self.playmp3(SuccessfullyConnectedWithGroundVehicleMP3File)

        MyCopter = USB1Vehicle

        self.playmp3(TelemetryMP3File)

        while(1) :

            if MyCopter.mode.name == "GUIDED"  :  
                self.playmp3(StartTrackingMP3File)
                break


        while(1) :

            if MyCopter.mode.name == "GUIDED" :

                dest = LocationGlobalRelative(Rover.location.global_frame.lat, Rover.location.global_frame.lon, PYJAltitude)
                MyCopter.simple_goto(dest)

                self.playmp3(GPSConditionMP3File)

                time.sleep(1)

            if MyCopter.mode.name != "GUIDED" :
                self.playmp3(WaitingMP3File)
                time.sleep(1)


        print " \n completed "

        self.playmp3(LandingMP3File)

    def run(self):
        self.do_flight()

competiton = Competition()
competiton.run()

sys.exit
