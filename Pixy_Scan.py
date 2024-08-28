"""Scans The Game Field To Find A Ball"""

import Scan
from pixycamev3.pixy2 import Pixy2
from time import sleep, time
from pixycamev3.pixy2 import Pixy2ConnectionError, Pixy2CommunicationError, Pixy2DataError

# Constants for the camera reference values
LEFT_X_REF_MIN_NORMAL = 48
LEFT_X_REF_MAX_NORMAL = 137
MIDDLE_X_REF_MIN_NORMAL = 138
MIDDLE_X_REF_MAX_NORMAL = 246
RIGHT_X_REF_MIN_NORMAL = 247
RIGHT_X_REF_MAX_NORMAL = 309

LEFT_X_REF_MIN_BACK = 40
LEFT_X_REF_MAX_BACK = 110
MIDDLE_X_REF_MIN_BACK = 115
MIDDLE_X_REF_MAX_BACK = 190
RIGHT_X_REF_MIN_BACK = 195
RIGHT_X_REF_MAX_BACK = 255

# Signature for the ball we're interested in
ORANGE_BALL_SIGNATURE = 1
PURPLE_BALL_SIGNATURE = 2

# Create the object for the camera
pixy = Pixy2(port=1, i2c_address=0x54)

def scan_ball_position(blocks, mode):
    """Determines the position of the ball based on its x_center and mode."""
    if blocks[0].sig == ORANGE_BALL_SIGNATURE:
        x_center = blocks[0].x_center
        if mode == "normal":
            if LEFT_X_REF_MIN_NORMAL <= x_center <= LEFT_X_REF_MAX_NORMAL:
                return "left"
            elif MIDDLE_X_REF_MIN_NORMAL <= x_center <= MIDDLE_X_REF_MAX_NORMAL:
                return "middle"
            elif RIGHT_X_REF_MIN_NORMAL <= x_center <= RIGHT_X_REF_MAX_NORMAL:
                return "right"
            else:
                return False
        elif mode == "back":
            if LEFT_X_REF_MIN_BACK <= x_center <= LEFT_X_REF_MAX_BACK:
                return "go_home_left"
            elif MIDDLE_X_REF_MIN_BACK <= x_center <= MIDDLE_X_REF_MAX_BACK:
                return "go_home_middle"
            elif RIGHT_X_REF_MIN_BACK <= x_center <= RIGHT_X_REF_MAX_BACK:
                return "go_home_right"
            else:
                return False
    return False

def normal_camera_scan():
    """Scans for a ball in the normal game field."""
    while True:
        sleep(2)
        nr_blocks, blocks = pixy.get_blocks(ORANGE_BALL_SIGNATURE, 4)
        if nr_blocks > 0:
            position = scan_ball_position(blocks, "normal")
            if position:
                Scan.scan(position)
                continue
        else:                
            handle_no_ball()

def back_camera_scan():
    """Scans for a ball in the back game field."""
    while True:
        nr_blocks, blocks = pixy.get_blocks(ORANGE_BALL_SIGNATURE, 4)
        if nr_blocks > 0:
            position = scan_ball_position(blocks, "back")
            if position:
                Scan.scan(position)
                return True
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
    total_wait_time = 6  # seconds

    while time() - start_time < total_wait_time:
        nr_blocks, blocks = pixy.get_blocks(ORANGE_BALL_SIGNATURE, 4)
        if nr_blocks > 0:
            return  # Ball detected, exit the function

        sleep(check_interval)  # Wait before checking again

    # No ball detected within the 6-second window, proceed with normal handling
    Scan.scan("go_back_to_scan")

