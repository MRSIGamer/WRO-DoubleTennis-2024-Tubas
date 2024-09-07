"""Scans The Game Field To Find A Ball"""

import Scan
from pixycamev3.pixy2 import Pixy2
from time import sleep, time
from pixycamev3.pixy2 import Pixy2ConnectionError, Pixy2CommunicationError, Pixy2DataError

# Constants for the camera reference values
LEFT_X_REF_MIN_NORMAL = 0
LEFT_X_REF_MAX_NORMAL =  120
MIDDLE_X_REF_MIN_NORMAL = 121
MIDDLE_X_REF_MAX_NORMAL = 200
RIGHT_X_REF_MIN_NORMAL = 201
RIGHT_X_REF_MAX_NORMAL = 300



MAX_Y_REF = 200
MIN_Y_REF = 55

MIN_Y_REF_BACK = 55
MAX_Y_REF_BACK = 200


LEFT_X_REF_MIN_BACK = 30
LEFT_X_REF_MAX_BACK = 107
MIDDLE_X_REF_MIN_BACK = 109
MIDDLE_X_REF_MAX_BACK = 169
RIGHT_X_REF_MIN_BACK = 170
RIGHT_X_REF_MAX_BACK = 233

# Signature for the ball we're interested in
ORANGE_BALL_SIGNATURE = 1
PURPLE_BALL_SIGNATURE = 2
PURPLE_AND_ORANGE_BALL_SIG_MAP = 3

# Create the object for the camera
pixy = Pixy2(port=1, i2c_address=0x54)



def get_orange_and_purple_ball_cordinatees(blocks : list):

    filtered_blocks = []
    filterd_left_side_list = []


    
                                                 
                    






                    # filtered_blocks.append(block)
                    # if len(filtered_blocks) >= blocks:
                    #     return filtered_blocks
                    # elif not filtered_blocks:
                    #     return False


def get_purple_ball_index(filtered_blocks : int):
    if filtered_blocks:
        for index, filtered_block in enumerate(filtered_blocks, 0):
            if filtered_block.sig == 2:
                return index   
    elif not filtered_blocks:
        return False
    




def scan_ball_position(blocks, mode):
    """Determines the position of the ball based on its x_center and mode."""
    x_center = blocks[0].x_center
    y_center = blocks[0].y_center
    if mode == "normal":
        if MIN_Y_REF <= y_center <= MAX_Y_REF:
            if blocks[0].sig == 1:
                if LEFT_X_REF_MIN_NORMAL <= x_center <= LEFT_X_REF_MAX_NORMAL:
                    return "left"
                elif MIDDLE_X_REF_MIN_NORMAL <= x_center <= MIDDLE_X_REF_MAX_NORMAL:
                    return "middle"
                elif RIGHT_X_REF_MIN_NORMAL <= x_center <= RIGHT_X_REF_MAX_NORMAL:
                    return "right"
                else:
                    return False
                

            if blocks[0].sig == 2:
                if LEFT_X_REF_MIN_NORMAL <= x_center <= LEFT_X_REF_MAX_NORMAL:
                    return "go_to_pp_ball_left"
                elif MIDDLE_X_REF_MIN_NORMAL <= x_center <= MIDDLE_X_REF_MAX_NORMAL:
                    return "get_pp_ball_middle"
                elif RIGHT_X_REF_MIN_NORMAL <= x_center <= RIGHT_X_REF_MAX_NORMAL:
                    return "go_to_pp_bal_right"
                else:
                    return False




    elif mode == "back":
        if MIN_Y_REF_BACK <= y_center <= MAX_Y_REF_BACK:
            if blocks[0].sig == 1:
                if LEFT_X_REF_MIN_BACK <= x_center <= LEFT_X_REF_MAX_BACK:
                    return "go_home_left"
                elif MIDDLE_X_REF_MIN_BACK <= x_center <= MIDDLE_X_REF_MAX_BACK:
                    return "go_home_middle"
                elif RIGHT_X_REF_MIN_BACK <= x_center <= RIGHT_X_REF_MAX_BACK:
                    return "go_home_right"
                else:
                    return False
                
            
            if blocks[0].sig == 2:
                if LEFT_X_REF_MIN_BACK <= x_center <= LEFT_X_REF_MAX_BACK:
                    return "go_home_left_pp_ball"
                elif MIDDLE_X_REF_MIN_BACK  <= x_center <= MIDDLE_X_REF_MAX_BACK:
                    return "go_home_middle_pp_ball"
                elif RIGHT_X_REF_MIN_BACK <= x_center <= RIGHT_X_REF_MAX_BACK:
                    return "go_home_right_pp_ball"
                else:
                    return False
            

        


def normal_camera_scan():
    """Scans for a ball in the normal game field."""
    while True:
        sleep(2)
        nr_blocks, blocks = pixy.get_blocks(3, 2)
        if nr_blocks == 1:
            position = scan_ball_position(blocks, "normal")
            if position:
                Scan.scan(position)
                return True
        
        elif nr_blocks > 1:
            if blocks[0].sig == 2 and blocks[1].sig == 1 or blocks[0].sig == 1 and blocks[1].sig == 2:
                if MIN_Y_REF <= blocks[0].y_center and blocks[1].y_center  <= MAX_Y_REF:
                    if LEFT_X_REF_MIN_NORMAL <= blocks[0].x_center <= LEFT_X_REF_MAX_NORMAL and LEFT_X_REF_MIN_NORMAL <= blocks[1].x_center <= LEFT_X_REF_MAX_NORMAL:
                        Scan.scan("left_pp_and_o_ball")
                        return True
                    elif MIDDLE_X_REF_MIN_NORMAL <= blocks[0].x_center <= MIDDLE_X_REF_MAX_NORMAL and MIDDLE_X_REF_MIN_NORMAL <= blocks[1].x_center <= MIDDLE_X_REF_MAX_NORMAL:
                        Scan.scan("middle_pp_and_o_ball")
                        return True

                    elif RIGHT_X_REF_MIN_NORMAL <= blocks[0].x_center <= RIGHT_X_REF_MAX_NORMAL and RIGHT_X_REF_MIN_NORMAL <= blocks[1].x_center <= RIGHT_X_REF_MAX_NORMAL:
                        Scan.scan("right_pp_and_o_ball")
                        return True
                    
                    
                    else:
                        position = scan_ball_position(blocks, "normal")
                        if position:
                            Scan.scan(position)
                            return True
                        return False
            
            else:
                position = scan_ball_position(blocks, "normal")
                if position:
                    Scan.scan(position)
                    return True
                return False

        else:                
            handle_no_ball()




def back_camera_scan():
    """Scans for a ball in the back game field."""
    while True:
        sleep(1)
        nr_blocks, blocks = pixy.get_blocks(ORANGE_BALL_SIGNATURE, 4)
        if nr_blocks == 1:
            position = scan_ball_position(blocks, "back")
            if position:
                Scan.scan(position)
                return True
            return False
        elif nr_blocks > 2:
            if blocks[0].sig == 2 and blocks[1].sig == 1 or blocks[0].sig == 1 and blocks[1].sig == 2:
                if MIN_Y_REF_BACK <= blocks[0].y_center and blocks[1].y_center <= MAX_Y_REF_BACK:
                    if LEFT_X_REF_MIN_BACK <= blocks[0].x_center <= LEFT_X_REF_MAX_BACK and LEFT_X_REF_MIN_BACK <= blocks[1].x_center <= LEFT_X_REF_MAX_BACK:
                        Scan.scan("left_pp_and_o_ball")
                        return True

                    elif MIDDLE_X_REF_MIN_BACK <= blocks[0].x_center <= MIDDLE_X_REF_MAX_BACK and MIDDLE_X_REF_MIN_BACK <= blocks[1].x_center <= MIDDLE_X_REF_MAX_BACK:
                        Scan.scan("middle_pp_and_o_ball")
                        return True

                    elif RIGHT_X_REF_MIN_BACK <= blocks[0].x_center <= RIGHT_X_REF_MAX_BACK and RIGHT_X_REF_MIN_BACK <= blocks[1].x_center <= RIGHT_X_REF_MAX_BACK:
                        Scan.scan("right_pp_and_o_ball")
                        return True

                    else:
                        position = scan_ball_position(blocks, "back")
                        if position:
                            Scan.scan(position)
                            return True
                else:
                    return False
            else:
                return False
        else:
            return False


def purple_ball_camera_scan():
    while True:
        sleep(1)
        nr_blocks, blocks = pixy.get_blocks([1,3], 1)

        if blocks[0] > 0:
            if blocks[0].sig == 3:
                return True
            elif blocks[0].sig == 1:
                return False
        else:   
            return False
        



def handle_no_ball():
    """Handles the case when no ball is detected in the normal scan."""
    start_time = time()
    check_interval = 2  # seconds
    total_wait_time = 10  # seconds

    while time() - start_time < total_wait_time:
        nr_blocks, blocks = pixy.get_blocks(ORANGE_BALL_SIGNATURE, 4)
        if nr_blocks > 0:
            return  # Ball detected, exit the function

        sleep(check_interval)  # Wait before checking again

    # No ball detected within the 6-second window, proceed with normal handling
    Scan.scan("go_back_to_scan")

 