#!/usr/bin/env python3

from time import sleep
import time     
from Movement_Methods import Movement
from ev3dev2.motor import MediumMotor, LargeMotor,OUTPUT_A, OUTPUT_B,OUTPUT_D ,OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
from pixycamev3.pixy2 import Pixy2
from Start import start_game
from Pixy_Scan import normal_camera_scan
from Pixy_Scan import back_camera_scan
from Stop_Game import Stop_Game
from pixycamev3.pixy2 import Pixy2ConnectionError
from pixycamev3.pixy2 import Pixy2CommunicationError
from pixycamev3.pixy2 import Pixy2DataError
from Blind_Scan import blind_scan
from ev3dev2.sound import Sound
import Scan
speaker = Sound()
movement = Movement()

#Initilizing The Pixy
pixy2 = Pixy2(port=1,i2c_address=0x54)


def get_Ball_pos():
    while True:
        # Retrieve the number of detected blocks and the block data
        sleep(1)
        nr_blocks, blocks = pixy2.get_blocks(1, 3)
        if nr_blocks == 1:
            print(blocks[0].y_center)

        if nr_blocks == 0:
            print("no")


#Variables To Setup A Timer
start_time= time.time()
duration = 120 # seconds


def main_game_with_pixy():
    """Makes A Full 2 Mins Game Using The Pixy"""
    start_game()
    while time.time() - start_time < duration:
        normal_camera_scan()

    else:
        Stop_Game()
        quit()

LEFT_X_REF_MIN_NORMAL = 22
LEFT_X_REF_MAX_NORMAL =  98
MIDDLE_X_REF_MIN_NORMAL = 99
MIDDLE_X_REF_MAX_NORMAL = 186
RIGHT_X_REF_MIN_NORMAL = 187
RIGHT_X_REF_MAX_NORMAL = 273



        
if __name__ == "__main__":

    speaker.play_file("rampbotsound.wav")
    print("started")

    #Checks The Touch Sensor Is Pr5essed Then Released To Start The Game
    while True:
        
        if movement.TouchSensor.is_pressed:
            while True:
                if movement.TouchSensor.is_released:
                    while True:
                        get_Ball_pos()