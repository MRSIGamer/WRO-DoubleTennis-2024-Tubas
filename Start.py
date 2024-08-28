"""Starts The Game Using The Pixy Cam(If Connected Correctly If Not It Will Start The Game Blindly)"""

from time import sleep
from Scan import scan
from pixycamev3.pixy2 import Pixy2



start_left_ref_min = 30
start_left_ref_max = 190
start_right_ref_min = 220
start_right_ref_max = 350

pixy = Pixy2(port=1, i2c_address=0x54)


def start_game():
    while True:
        nr_blocks, blocks = pixy.get_blocks(1, 2)
        if nr_blocks == 2:
            if blocks[0].sig == 1 and blocks[1].sig == 1:
                    #checks if the ball is in the start_left area
                    if start_right_ref_min < blocks[0].x_center < start_right_ref_max and start_right_ref_min < blocks[1].x_center < start_right_ref_max:
                        scan("start_right")
                        return True
                
                    elif start_left_ref_min < blocks[0].x_center < start_left_ref_max and start_right_ref_min < blocks[1].x_center < start_right_ref_max:
                        scan("start_left")
                        scan("start_right")
                        return True

                    elif start_left_ref_min < blocks[1].x_center < start_left_ref_max and start_right_ref_min < blocks[0].x_center < start_right_ref_max:
                        scan("start_left")
                        scan("start_right")
                        return True


        if nr_blocks == 1:
            if blocks[0].sig == 1:
                    

                    #checks if the ball is in the start_left area
                    if start_left_ref_min < blocks[0].x_center < start_left_ref_max: 
                        scan("start_left_2")
                        return True
                    



