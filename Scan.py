"""Makes A Linear Search To Extract The Ball From"""

from Movement_Methods import Movement
from Movement_Methods import *
import random as rd
from Pixy_Scan import back_camera_scan, purple_ball_camera_scan
from time import sleep
movement = Movement()



def Go_Home():
    """A function that makes the robot go to home in all the scans"""
    movement.GyroSensor.reset()
    movement.Gyro_Straight_Move_Until_Stalled(20)
    movement.Long_Turn(-20, 85)
    movement.Drive_Untill_Stalled(-20)
    movement.Drive_Straight_Degs(20, 290)
    movement.Turn(10, 85)
    movement.Drive_Untill_Stalled(-20)
    movement.Turn_Hiter_Back()

def Go_Home_For_Start():
    """A function that makes the robot go to home only in Start Left Scan"""
    movement.GyroSensor.reset()
    movement.Gyro_Straight_Move_Until_Stalled(20)
    movement.Long_Turn(-20, 85)
    movement.Drive_Untill_Stalled(-20)
    movement.Drive_Straight_Degs(20, 395)
    movement.Turn(10, 80)
    movement.Drive_Untill_Stalled(-10)
    movement.Turn_Hiter_Back()




#A method that search is different areas in the game field
def scan(area : str):
    """Get The Balls In Left AB : "start_left". 
       Get The Balls In Right AB : "start_right". 
       Whole Left Area : "left". 
       Whole Middle Area : "middle". 
       Whole Right Area : "right". 
       Whole Left Next To Home Area : "go_home_left"
       Whole Middle Next To Home Area : "go_home_middle"
       Whole Right Next To Home Area : "go_home_right"
       Go To The Middle Of The Mat To Checks if there is Balls In The Home: "go_back_to_scan" 
       """
       
    
    choice = -1

    
    while True:
        #Checks if the user want to scan the right A,B ball section
        if area.lower().replace(" ", "") == "start_right":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, 35)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Long_Turn(10, -35)
            movement.Gyro_Straight_Move_Degs(20, 150)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 30)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Turn(10, -85)
            movement.Drive_Untill_Stalled(-20)
            movement.Drive_Straight_Degs(10, 140)
            movement.Spin_90_Degrees_Left()
            movement.Long_Turn(10, 70)
            movement.Long_Turn(10, -70)
            movement.Drive_Straight_Degs(-10, 220)
            sleep(1)
            Scan = back_camera_scan()
            if not Scan:
                Go_Home()
                break
            
            

            

        #Checks if the user want to catch the balls in the left A,B ball section
        elif area.lower().replace(" ", "") == "start_left":
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 500)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.6)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            sleep(1)
            scan = back_camera_scan()
            if not scan:
                Go_Home_For_Start()
                break


        #Checks if the user want to catch the balls in the left A,B ball section
        elif area.lower().replace(" ", "") == "start_left_2":
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(10, 500)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.6)
            purple_ball_scan = purple_ball_camera_scan()
            
            if purple_ball_scan:
                movement.Gyro_Straight_Move_Degs(20, 300)
                movement.Catch_Ball()
                movement.Spin_90_Degrees_Right()
                movement.Drive_Untill_Stalled(-20)
                movement.Gyro_Straight_Move_Degs(20, 300)
                movement.Spin_90_Degrees_Right()
                Go_Home()
                movement.Long_Turn(20, -85)
                movement.Gyro_Straight_Move_Degs(20, 220)
                sleep(0.5)
                movement.Open_Catcher()
                movement.Drive_Untill_Stalled(-20)
                movement.Gyro_Straight_Move_Degs(20, 280)
                movement.Spin_90_Degrees_Right()
                movement.Drive_Untill_Stalled(-20)
                break


            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            sleep(1)
            scan = back_camera_scan()
            if not scan:
                Go_Home()
                break

    
        #Checks if the user wants the robot to go to the middle area
        elif area.lower().replace(" ", "") == "middle" or choice == 2: 
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 700)
            sleep(0.9)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 150)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            sleep(1)
            scan = back_camera_scan()
            if not scan:
                Go_Home()
                break


        #checks if the user wants the robot to go to the left section in the mat
        elif area.lower().replace(" ", "") == "left" or choice == 1:
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, -20)
            movement.Drive_Straight_Degs(25, 785)
            sleep(0.8)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 150)
            movement.Turn(10, 5)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            sleep(1)
            scan = back_camera_scan()
            if not scan:
                Go_Home()
                break


        #Checks if the user wants the robot to go to the right section of the mat
        elif area.lower().replace(" ", "") == "right" or choice == 3:
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, 30)
            movement.Drive_Straight_Degs(20, 800)
            sleep(0.7)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250)
            movement.Long_Turn(10, -10)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Long_Turn(10, 10) 
            movement.Long_Turn(10, -80)
            movement.Drive_Untill_Stalled(-20)
            movement.Drive_Straight_Degs(10, 140)
            movement.Spin_90_Degrees_Left()
            movement.Long_Turn(10, 70)
            movement.Long_Turn(10, -70)
            movement.Drive_Straight_Degs(-10, 325)
            sleep(1)
            scan = back_camera_scan()
            if not scan:
                Go_Home()
                break
            


        #Checks if the user wants the robot to go to the middle next to home section of the mat
        elif area.lower().replace(" ", "") == "go_home_middle":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Gyro_Straight_Move_Until_Stalled(30)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(10, 200)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Drive_Untill_Stalled(-10)
            movement.Turn_Hiter_Back()
            break


        #Checks if the user wants the robot to go to the left next to home section of the mat
        elif area.lower().strip().replace(" ", "") == "go_home_left":
            movement.Turn_Hiter_Back()
            sleep(0.4)  
            movement.Turn(10, -30)
            movement.Drive_Untill_Stalled(30)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250)
            movement.Long_Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(10, 200)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Drive_Untill_Stalled(-10)
            movement.Turn_Hiter_Back()
            break

        #Checks if the user wants the robot to go to the right next to home section of the mat
        elif area.lower().replace(" ", "").strip() == "go_home_right":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Turn(10, 10)
            movement.Drive_Untill_Stalled(30)
            sleep(0.4)
            movement.Long_Turn_Untill_Stalled(30, 0)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 40)
            movement.Long_Turn(-10, -40)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(10, 200)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Drive_Untill_Stalled(-10)
            movement.Turn_Hiter_Back()
            break


        #Checks if the user wants the robot to go to the middle of the mat to checks if  a ball exists there
        elif area.lower().replace(" ", "").strip() == "go_back_to_scan":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Gyro_Straight_Move_Degs(35 , 700)
            movement.Catch_Ball()
            sleep(0.4)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Spin_90_Degrees_Right()
            scan = back_camera_scan()
            if not scan:
                Go_Home()
                break
            
            
        
        # Checks if the user wants the robot to take the purple ball from the left A start section of the mat
        elif area.replace(" ", "").lower() == "get_pp_bal_left_b":
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 500)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.6)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Catch_Ball()
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Spin_90_Degrees_Right()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break

        
        # Checks if the user wants the robot to take the purple ball from the left B start section of the mat
        elif area.replace(" ", "").lower() == "get_pp_bal_left_a":
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 500)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 100)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Spin_90_Degrees_Right()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break

        # Checks if the user wants the robot to take the purple ball from the right B start section of the mat
        elif area.replace(" ", "").lower() == "get_pp_bal_right_a":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(20, 35)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Long_Turn(20, -35)
            movement.Gyro_Straight_Move_Degs(20, 150)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 100)
            movement.Long_Turn(20, -85)
            movement.Spin_90_Degrees_Left()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break


        # Checks if the user wants the robot to take the purple ball from the right A start section of the mat
        elif area.replace(" ", "").lower() == "get_pp_bal_right_b":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(20, 35)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Long_Turn(20, -35)
            movement.Gyro_Straight_Move_Degs(20, 150)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 100)
            movement.Throw_Ball()
            sleep(0.4)
            movement.Turn_Hiter_Back()
            sleep(0.6)
            movement.Gyro_Straight_Move_Degs(20, 300)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 200)
            movement.Long_Turn(20, -85)
            movement.Spin_90_Degrees_Left()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break




        #Checks if the user wants the robot to go to the middle area to take the purple ball
        elif area.lower().replace(" ", "") == "get_pp_ball_middle": 
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 700)
            sleep(0.9)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 150)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break


        #checks if the user wants the robot to go to the left section in the mat to take the purple ball
        elif area.lower().replace(" ", "") == "go_to_pp_ball_left":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, -20)
            movement.Drive_Straight_Degs(25, 785)
            sleep(0.8)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 150)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break




        #Checks if the user wants the robot to go to the right section of the mat
        elif area.lower().replace(" ", "") == "go_to_pp_bal_right":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, 30)
            movement.Drive_Straight_Degs(20, 800)
            sleep(0.7)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250) 
            movement.Long_Turn(10, -80)
            movement.Drive_Untill_Stalled(-20)
            movement.Drive_Straight_Degs(10, 140)
            movement.Spin_90_Degrees_Left()
            movement.Long_Turn(10, 70)
            movement.Long_Turn(10, -70)
            Go_Home()
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break



        # Checks if the user wants the robot to go to the middle next to home section of the mat to take the purple ball
        elif area.lower().replace(" ", "") == "go_home_middle_pp_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Gyro_Straight_Move_Until_Stalled(30)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break




        #Checks if the user wants the robot to go to the left next to home section of the mat to take the purble ball
        elif area.lower().strip().replace(" ", "") == "go_home_left_pp_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)  
            movement.Turn(10, -30)
            movement.Drive_Untill_Stalled(30)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250)
            movement.Long_Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break


        #Checks if the user wants the robot to go to the right next to home section of the mat to take the purble ball
        elif area.lower().replace(" ", "").strip() == "go_home_right_pp_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Turn(10, 10)
            movement.Drive_Untill_Stalled(30)
            sleep(0.4)
            movement.Long_Turn_Untill_Stalled(30, 0)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 40)
            movement.Long_Turn(-10, -40)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Long_Turn(20, -85)
            movement.Gyro_Straight_Move_Degs(20, 220)
            sleep(0.5)
            movement.Open_Catcher()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            break



        #checks if the user wants the robot to go to the left section in the mat if there is an orange and purble balls 
        elif area.lower().replace(" ", "") == "left_pp_and_o_ball":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, -20)
            movement.Drive_Straight_Degs(25, 785)
            sleep(0.8)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-20, 150)
            movement.Turn(10, 5)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            Go_Home()
            movement.Throw_Ball_Weakly()
            break





        #Checks if the user wants the robot to go to the middle area to take the purble ball
        elif area.lower().replace(" ", "") == "middle_pp_and_o_ball": 
            movement.Turn_Hiter_Back()
            movement.Gyro_Straight_Move_Degs(20, 700)
            sleep(0.9)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 150)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 300)
            movement.Spin_90_Degrees_Right()
            movement.Drive_Straight_Degs(-10 , 200)
            Go_Home()
            movement.Throw_Ball_Weakly()
            break




        #Checks if the user wants the robot to go to the right section of the mat to take the purble ball if it is next to an orange ball
        elif area.lower().replace(" ", "") == "right_pp_and_o_ball":
            movement.Turn_Hiter_Back()
            movement.Long_Turn(10, 30)
            movement.Drive_Straight_Degs(20, 800)
            sleep(0.7)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250)
            movement.Long_Turn(10, -85)
            movement.Drive_Untill_Stalled(-20)
            movement.Drive_Straight_Degs(10, 140)
            movement.Spin_90_Degrees_Left()
            movement.Long_Turn(10, 70)
            movement.Long_Turn(10, -70)
            movement.Drive_Straight_Degs(-10, 325)
            Go_Home()
            movement.Throw_Ball_Weakly()
            break




        #Checks if the user wants the robot to go to the middle next to home section of the mat to take the purple ball if it is next to an orange ball
        elif area.lower().replace(" ", "") == "go_home_middle_pp_and_o_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Gyro_Straight_Move_Until_Stalled(30)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Gyro_Straight_Move_Degs(20, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Throw_Ball_Weakly()
            break


        #Checks if the user wants the robot to go to the left next to home section of the mat to take the purple ball if it is next to an orange ball
        elif area.lower().strip().replace(" ", "") == "go_home_left_pp_and_o_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)  
            movement.Turn(10, -30)
            movement.Drive_Untill_Stalled(30)
            movement.Catch_Ball()
            movement.Drive_Straight_Degs(-10, 250)
            movement.Long_Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Throw_Ball_Weakly()
            break


        #Checks if the user wants the robot to go to the right next to home section of the mat to take the purple ball if it is next to an orange ball
        elif area.lower().replace(" ", "").strip() == "go_home_right_pp_and_o_ball":
            movement.Turn_Hiter_Back()
            sleep(0.4)
            movement.Turn(10, 10)
            movement.Drive_Untill_Stalled(30)
            sleep(0.4)
            movement.Long_Turn_Untill_Stalled(30, 0)
            movement.Catch_Ball()
            movement.Long_Turn(-10, 40)
            movement.Long_Turn(-10, -40)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-20)
            movement.Gyro_Straight_Move_Degs(10, 280)
            movement.Turn(10, 85)
            movement.Drive_Untill_Stalled(-10)
            movement.Throw_Ball_Weakly()
            break







        else:
            choice = rd.randint(1, 3)
            if choice == 1:
                area == "left"
                continue

            if choice == 2:
                area == "middle"
                continue

            if choice == 3:
                area == "right"
                continue
