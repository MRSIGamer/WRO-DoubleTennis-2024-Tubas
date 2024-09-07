"""Starts The Game Using The Pixy Cam(If Connected Correctly If Not It Will Start The Game Blindly)"""

from time import sleep
from Scan import scan
from pixycamev3.pixy2 import Pixy2


MAX_Y_REF = 200
MIN_Y_REF = 55


start_left_ref_min = 30
start_left_ref_max = 190
start_right_ref_min = 220
start_right_ref_max = 350
left_ball_y_ref_min_A = 96
left_ball_y_ref_max_A = 115
left_ball_y_ref_min_B = 74
left_ball_y_ref_max_B = 90
right_ball_y_ref_min_A = 100
right_ball_y_ref_max_A = 120
right_ball_y_ref_min_B = 75
right_ball_y_ref_max_B = 95



pixy = Pixy2(port=1, i2c_address=0x54)


#Gets the purple ball index in the blocks list
def get_purple_ball_index(blocks : list):
    """Searching for the purple block index / place in the blocks list since there is no way to find it"""
    for block in blocks:
        if block.sig == 2:
            try:
                if MIN_Y_REF <= block.y_center <= MAX_Y_REF:
                    return block
                else:
                    return False 
            except AttributeError:
                return 1
                

def start_game():
    """Starting The Game Using The Pixy Cam"""

    while True:
        nr_blocks, blocks = pixy.get_blocks(3, 3)

        #Checks if there is only 2 balls in the start of the game and that means that there is no purple balls in the robot side
        if nr_blocks == 2:
            if blocks[0].sig == 1 and blocks[1].sig == 1:
                if MIN_Y_REF <= blocks[0].y_center and blocks[1].y_center <= MAX_Y_REF:

                    #checks if the ball is in the start_left area
                    if start_right_ref_min < blocks[0].x_center < start_right_ref_max and start_right_ref_min < blocks[1].x_center < start_right_ref_max:
                        scan("quick_start_right")
                        return True
                
                    elif start_left_ref_min < blocks[0].x_center < start_left_ref_max and start_right_ref_min < blocks[1].x_center < start_right_ref_max:
                        scan("quick_start_left2")
                        scan("quick_start_right")
                        return True

                    elif start_left_ref_min < blocks[1].x_center < start_left_ref_max and start_right_ref_min < blocks[0].x_center < start_right_ref_max:
                        scan("quick_start_left2")
                        scan("quick_start_right")
                        return True
                    

                    elif start_left_ref_min <= blocks[0].x_center <= start_left_ref_max and start_left_ref_min <= blocks[1].x_center <= start_left_ref_max:
                        scan("quick_start_left")
                        return True
                    
        

        #Checks if the number of balls in the start is 3 since that means that the robot has a purple ball in his field
        elif nr_blocks == 3:
            pp_index = get_purple_ball_index(blocks)

            if pp_index:
                if start_left_ref_min <= pp_index.x_center <= start_left_ref_max and left_ball_y_ref_min_A <= pp_index.y_center <= left_ball_y_ref_max_A:
                    scan("get_pp_bal_left_a")
                    scan("quick_start_left2")
                    scan("quick_start_right")
                    return True
                


                if start_left_ref_min <= pp_index.x_center <= start_left_ref_max and left_ball_y_ref_min_B <= pp_index.y_center <= left_ball_y_ref_max_B:
                        scan("get_pp_bal_left_b")
                        scan("quick_start_right")
                        return True



                elif start_right_ref_min <= pp_index.x_center <= start_right_ref_max and right_ball_y_ref_min_A <= pp_index.y_center <= right_ball_y_ref_max_A:
                    scan("get_pp_bal_right_a")
                    scan("quick_start_left2")
                    scan("quick_start_right")
                    return True




                elif start_right_ref_min <= pp_index.x_center <= start_right_ref_max and right_ball_y_ref_min_B <= pp_index.y_center <= right_ball_y_ref_max_B:
                        scan("get_pp_bal_right_b")
                        scan("quick_start_left")
                        return True

            
            #Handeling any error using the exeptional handeling
            elif pp_index == 1:
                continue


            else:
                continue

                

                        




             


        elif nr_blocks == 1:
            if blocks[0].sig == 1:
                if  MIN_Y_REF <= blocks[0].y_center <= MAX_Y_REF:
          

                    #checks if the ball is in the start_left area
                    if start_left_ref_min < blocks[0].x_center < start_left_ref_max: 
                        scan("quick_start_left")
                        return True
                        



