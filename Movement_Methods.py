#!/usr/bin/env python3
'''The module that include all the movments we need for the main algorithm'''
from ev3dev2.motor import MediumMotor, LargeMotor,OUTPUT_A, OUTPUT_B,OUTPUT_D ,OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
import ev3dev2.motor as motor
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, TouchSensor, ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_4,INPUT_2,INPUT_3
from time import sleep
import time
import logging
import random



class Movement:
    """This class contains all the general movements we need to make the search"""
    def __init__(self):
        #Motors | Outputs
        self.left_Motor = MediumMotor(OUTPUT_B)
        self.right_Motor = MediumMotor(OUTPUT_C)
        self.hiter_Motor = LargeMotor(OUTPUT_A)
        self.catcher_Motor = MediumMotor(OUTPUT_D)
        #DriveBase(MoveTank) | SteerBase(MoveSteering)
        self.DriveBase = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=MediumMotor)
        self.SteerBase = MoveSteering(OUTPUT_B, OUTPUT_C, motor_class = MediumMotor)
        self.ReversedSteerBase = MoveSteering(OUTPUT_C, OUTPUT_B, motor_class = MediumMotor)
        #Setting up motors
        self.right_Motor.polarity = MediumMotor.POLARITY_INVERSED
        #Sensors | Inputs
        self.GyroSensor = GyroSensor(INPUT_4)
        self.RampGyroSensor = GyroSensor(INPUT_2)
        self.TouchSensor = TouchSensor(INPUT_3)
        #Setting up sensors
        self.GyroSensor.reset()
        self.GyroSensor.calibrate()
        self.RampGyroSensor.reset()
        self.RampGyroSensor.calibrate()
        

    #A method that spins the robot exactly 90 degrees to the right using the gyro sensor
    def Spin_90_Degrees_Right(self):
        """Spins 90 Degrees To The Right Using Gyro"""
        gyro_angle = self.GyroSensor.angle
        while (self.GyroSensor.angle - gyro_angle) < 85:
            self.DriveBase.on(10, -10)
        else:
            self.DriveBase.stop(brake=True)


    #A method that spins the robot exactly 90 degrees to the left using the gyro sensor
    def Spin_90_Degrees_Left(self):
        """Spin 90 Degrees To The Left Using The Gyro Sensor"""
        gyro_angle = self.GyroSensor.angle
        while (self.GyroSensor.angle - gyro_angle) > -85:
            self.DriveBase.on(-10, 10)
        else:
            self.DriveBase.stop(brake=True)    


    #A method that spins the robot 180 degrees to the right
    def Spin_180_Degrees_Right(self):
        """Spin 180 Degrees To The Right Using The Gyro Sensor"""
        gyro_angle = self.GyroSensor.angle
        while (self.GyroSensor.angle - gyro_angle) < 185:
            self.DriveBase.on(10,-10)
        else:
            self.DriveBase.stop(brake=True)


    #A method that moves the robot straight forward or backward
    def Drive_Straight_Degs(self, speed : int, degrees : int):
        """Move The Robot Straight Forward Or Backward"""
        self.DriveBase.on_for_degrees(speed, speed, degrees, True, True)


    #A method that moves the robot straight forward or backward until the robot is stuck
    def Drive_Untill_Stalled(self, speed : int):
        """Drive The Robot Untill The Motor Is Stalled(stuck)"""
        while not self.DriveBase.is_stalled:
            self.DriveBase.on(speed,speed)
        else:
            self.DriveBase.stop(brake=True)
    

    #A method that moves the robot straight forward or backward untill you stop the robot
    def Drive_Straight(self, speed : int):
        self.DriveBase.on(speed, speed)


    #A method that turns the robot to a specific degree using the gyro sensor
    def Turn(self, speed : int, angle : int):
        """Turns The Robot To A Specific Angle Using Gyro"""
        if angle >= 0:
            gyro_angle = self.GyroSensor.angle
            while (self.GyroSensor.angle - gyro_angle) < angle:
                self.DriveBase.on(speed, -speed)
            else:
                self.DriveBase.stop(brake=True)
        elif angle < 0:
            gyro_angle = self.GyroSensor.angle
            while (self.GyroSensor.angle - gyro_angle) > angle:
                self.DriveBase.on(-speed,speed)
            else:
                self.DriveBase.stop(brake=True)


    #A method that moves only one motor to make a long turn using the gyro sensor
    def Long_Turn(self,speed : int, angle : int):
        """Makes A Long Turn By Rotating One Wheel A Time"""
        if angle > 0:
            if speed > 0:
                gyro_angle = self.GyroSensor.angle
                while (self.GyroSensor.angle - gyro_angle) < angle:
                    self.DriveBase.on(speed, 0)
                else:
                    self.DriveBase.stop(brake = True)
            elif speed < 0:
                gyro_angle = self.GyroSensor.angle
                while (self.GyroSensor.angle - gyro_angle) < angle:
                    self.DriveBase.on(0, speed)
                else:
                    self.DriveBase.stop(brake = True)
        if angle < 0:
            if speed > 0:
                gyro_angle = self.GyroSensor.angle
                while (self.GyroSensor.angle - gyro_angle) > angle:
                    self.DriveBase.on(0, speed)
                else:
                    self.DriveBase.stop(brake = True)
            elif speed < 0:
                gyro_angle = self.GyroSensor.angle
                while (self.GyroSensor.angle - gyro_angle) > angle:
                    self.DriveBase.on(speed, 0)
                else:
                    self.DriveBase.stop(brake = True)
    

    #A method that makes the robot makes a long turn by rotating one motor only
    def Long_Turn_Untill_Stalled(self, speed : int, direction : int):
        """Turns The Robot A Long Turn By Rotating One Wheel Only
            If Direction Is Equal To 1 The Robot Will Turn To The Right
            If Direction Is Equal To 0 The Robot Will Turn To The Left
        """
        while not self.DriveBase.is_stalled:
            if direction == 1:
                self.DriveBase.on(speed, 0)
            if direction == 0:
                self.DriveBase.on(0, speed)
        else:
            self.DriveBase.stop(brake=True)


    #A method that drives the robot straight using a pd follower with gyro sensor for a limited time
    def Drive_Straight_Untill_Ramping(self, speed : int):
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed And Degrees Should Be Positive only)
        """
 

        ramp_gyro_angle = self.RampGyroSensor.angle
        while (self.RampGyroSensor.angle - ramp_gyro_angle) > -3:
            self.DriveBase.on(speed, speed)
            sleep(0.5)
        else:
            self.DriveBase.stop(brake=True)
            self.Lift_Hiter()
  
        





    #A method that drives the robot straight using a pd follower with gyro sensor for a limited time
    def Gyro_Straight_Move_Untill_Ramping(self, speed : int):
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed And Degrees Should Be Positive only)
        """
        kp = 0.3
        ki = 0.01
        kd = 0.9

        target_angle = 0

        integral = 0
        last_error = 0


        max_speed = speed


        gyro_angle = self.RampGyroSensor.angle
        while  (self.RampGyroSensor.angle - gyro_angle) > -3:
            error = target_angle - self.GyroSensor.angle

            proportional = kp * error

            integral += error

            integral_term = ki * integral

            derivative = error - last_error

            derivative_term = kd * derivative

            turn_rate = proportional + integral_term + derivative_term
            turn_rate = max(-max_speed, min(max_speed, turn_rate))

            left_motor_speed = SpeedPercent(max_speed + turn_rate)
            right_motor_speed = SpeedPercent(max_speed - turn_rate)

            self.left_Motor.on(left_motor_speed)
            self.right_Motor.on(right_motor_speed)

            last_error = error

            max_speed += 1
            sleep(0.1)
        else:
            self.DriveBase.stop(brake=True)
            self.Lift_Hiter()




    #A method that drives the robot straight using a pd follower with gyro sensor for a limited time
    def Crazy_Gyro_Straight_Move_Untill_Ramping(self, speed : int):
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed And Degrees Should Be Positive only)
        """
        kp = 0.3
        ki = 0.01
        kd = 0.9

        target_angle = 0

        integral = 0
        last_error = 0


        max_speed = speed


        gyro_angle = self.RampGyroSensor.angle
        while  (self.RampGyroSensor.angle - gyro_angle) > -2:
            error = target_angle - self.GyroSensor.angle

            proportional = kp * error

            integral += error

            integral_term = ki * integral

            derivative = error - last_error

            derivative_term = kd * derivative

            turn_rate = proportional + integral_term + derivative_term
            turn_rate = max(-max_speed, min(max_speed, turn_rate))

            left_motor_speed = SpeedPercent(max_speed + turn_rate)
            right_motor_speed = SpeedPercent(max_speed - turn_rate)

            self.left_Motor.on(left_motor_speed)
            self.right_Motor.on(right_motor_speed)

            last_error = error

            max_speed += 2
            sleep(0.1)
        else:
            self.DriveBase.stop(brake=True)
            self.Lift_Hiter()





    #A method that drives the robot straight using a pd follower with gyro sensor for a limited time
    def Gyro_Straight_Move_Degs(self, speed : int, degrees : int):
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed And Degrees Should Be Positive only)
        """
        kp = 0.3
        ki = 0.01
        kd = 0.9

        target_angle = 0

        integral = 0
        last_error = 0


        max_speed = speed

        self.left_Motor.reset()
        self.GyroSensor.reset()
        while self.left_Motor.degrees < degrees:
            error = target_angle - self.GyroSensor.angle

            proportional = kp * error

            integral += error

            integral_term = ki * integral

            derivative = error - last_error

            derivative_term = kd * derivative

            turn_rate = proportional + integral_term + derivative_term
            turn_rate = max(-max_speed, min(max_speed, turn_rate))

            left_motor_speed = SpeedPercent(max_speed + turn_rate)
            right_motor_speed = SpeedPercent(max_speed - turn_rate)

            self.left_Motor.on(left_motor_speed)
            self.right_Motor.on(right_motor_speed)

            last_error = error

            sleep(0.01)
        else:
            self.DriveBase.stop(brake=True)


    #Same as "Gyro_Straight_Move_Degs" method but moves untill the robot is stalled
    def Gyro_Straight_Move_Until_Stalled(self, speed : int):
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed Should Be Positive only)
        """
        """Drives The Robot Very Straight Using A PD Follower With Gyro Sensor
           (The Speed And Degrees Should Be Positive only)
        """

        start_time= time.time()
        duration = 4.3 # seconds



        kp = 0.3
        ki = 0.01
        kd = 0.9

        target_angle = 0

        integral = 0
        last_error = 0


        max_speed = speed
        
        self.GyroSensor.reset()
        while time.time() - start_time < duration:
            error = target_angle - self.GyroSensor.angle

            proportional = kp * error

            integral += error

            integral_term = ki * integral

            derivative = error - last_error

            derivative_term = kd * derivative

            turn_rate = proportional + integral_term + derivative_term
            turn_rate = max(-max_speed, min(max_speed, turn_rate))

            left_motor_speed = SpeedPercent(max_speed + turn_rate)
            right_motor_speed = SpeedPercent(max_speed - turn_rate)

            self.DriveBase.on(left_motor_speed, right_motor_speed)

            last_error = error

            sleep(0.01)
            if self.DriveBase.is_stalled:
                break
    
        self.DriveBase.stop(brake=False)


    #A method that turn the robot 90 degrees to the left if the robot is moving exactly next to a wall
    def Turn_Left_Wall_90_Degs(self):
        """Turns Exactly 90 Degrees To The Left When The Robot Is Moving By A Wall"""
        gyro_angle = self.GyroSensor.angle
        while (self.GyroSensor.angle - gyro_angle) > -85:
            self.DriveBase.on(5, 25)
        else:
            self.DriveBase.stop(brake=True)


    #A method that turns the robot 90 degrees to the right if the robot is moving exactly next to a wall
    def Turn_Right_Wall_90_Degrees(self):
        """Turnns Exactly 90 Degrees To The Right When The Robot Is Moving By A Wall"""
        gyro_angle = self.GyroSensor.angle
        while (self.GyroSensor.angle - gyro_angle) < 80:
            self.DriveBase.on(35, 10)
        else:
            self.DriveBase.stop(brake=True)


    #A method that closes the catcher to catch a ball
    def Catch_Ball(self):
        """Closes the catcher to catch the ball in order to throw it"""
        while True:

            self.catcher_Motor.on(100, True, True)
            sleep(0.3)
            if self.catcher_Motor.is_stalled:
                self.catcher_Motor.stop()
                break
    
    
    #A method that opens the catcher to catch a ball
    def Open_Catcher(self):
        """Opens the catcher to throw the ball or realese it"""
        self.catcher_Motor.on(-100, True, True)
        if self.catcher_Motor.is_stalled:
            self.catcher_Motor.stop()
            return True
        


    #A method that opens the catcher to catch a ball
    def Open_Catcher_Without_Wait(self):
        """Opens the catcher to throw the ball or realese it"""
        self.catcher_Motor.on(-100, True, False)
        if self.catcher_Motor.is_stalled:
            self.catcher_Motor.stop()
            return True

    
    #A mthod that opens the catcher untill the motor stalls 
    def Open_Catcher_Untill_Stalled(self):
        """Opens The Catcher Untill The Catcher Motor Faces A Stall"""
        while not self.catcher_Motor.is_stalled:
            self.catcher_Motor.on(-100, True,True)
        else:
            self.catcher_Motor.stop()

    #A method that turns the hiter back
    def Turn_Hiter_Back(self):
        """Turns the hiter back to make sure that it throws the ball"""
        while True:
            self.hiter_Motor.on(100,True,True)
            if self.hiter_Motor.is_stalled:
                self.hiter_Motor.stop()
                break

    
    #A method that lifts the hiter motor up to throw the ball
    def Lift_Hiter(self):
        """Lifts The Hiter Up To Throw The Ball"""
        self.Lift_Hiter_To_Throw()
        self.Turn_Hiter_Back()


    #A method that lifts the hiter and the catcher up to throw the ball
    def Throw_Ball(self):
        """Lifts The  Catcher And Hiter Motors To  Throw The Ball"""
        self.Open_Catcher_Without_Wait()
        sleep(0.2)
        self.Lift_Hiter_To_Throw()
        self.Turn_Hiter_Back()


    #A method that lifts the hiter and the catcher up to throw the ball weakly
    def Throw_Ball_Weakly(self):
        """Lifts The  Catcher And Hiter Motors To Throw The Ball In A Weak Way"""
        self.hiter_Motor.on_for_degrees(100, 20, True,True)
        self.catcher_Motor.on_for_degrees(100,-165,True,False)
        sleep(0.2)
        self.hiter_Motor.on_for_degrees(-20, 100,True,True)


    def Throw_Ball_While_Running(self, speed : int, degrees : int, throw_degres : int):
        """Throws the ball while running to make a quick throw"""
        self.left_Motor.reset()
        while self.left_Motor.degrees < degrees:
            while self.left_Motor.degrees < throw_degres:
                self.DriveBase.on(speed, speed)
            else:
                self.Lift_Hiter()
                self.Gyro_Straight_Move_Degs(35, degrees - throw_degres)
                break
        else:
            self.DriveBase.stop(brake=True)



    def Throw_The_Ball_While_Driving(self, speed : int, degrees : int):
        "Lifts The Catcher and Hiter Motors To Throw The Ball While The Robot Is Moving"
        self.DriveBase.on_for_degrees(speed, speed, degrees, True, False)
        self.Throw_Ball()


    def Lift_Hiter_To_Throw(self):
        """Lifts The Hiter Up To Throw The Ball"""
        while True:
            self.hiter_Motor.on(-100, True, True)
            if self.hiter_Motor.is_stalled:
                self.hiter_Motor.stop()
                break
     


