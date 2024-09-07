#!/usr/bin/env python3


"""The Main Game File"""

#Importing The required modules
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


#Initilizing the speaker to play some sounds
speaker = Sound()

#Initilizing the movement class to use the touch sensor
movement = Movement()

#Initilizing The Pixy
pixy2 = Pixy2(port=1,i2c_address=0x54)



#Getting the balls X-Y to use it in the pixy code
def get_Ball_pos():
    """A function for debugging"""
    while True:
        # Retrieve the number of detected blocks and the block data
        sleep(1)

        nr_blocks, blocks = pixy2.get_blocks(1, 3)
        
        if nr_blocks == 1:
            print(blocks[0].x_center)
        if nr_blocks == 0:
            print("no") 






 



        
if __name__ == "__main__":

    #Plays a sound to notifiy team that the game has started 
    speaker.play_file("rampbotsound.wav")
    print("started")

    #Checks The Touch Sensor Is Pressed Then Released To Start The Game
    while True: 
        if movement.TouchSensor.is_pressed:
            if movement.TouchSensor.is_released:
                start_game()               
                while True:

                #     #Does the game for 30 second and after the 30 second the robot
                    start_time = time.time()
                    while time.time() - start_time < 30:
                        normal_camera_scan()
                    else:
                        Scan.scan("get_balls_from_the_corner")
                        continue