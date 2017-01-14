import wpilib

from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick

import robotmap

class DriveTrain(Subsystem):

    def __init__(self):
        super().__init__('Drive Train')

        self.frontLeftWheel = wpilib.Talon(robotmap.portsList.frontLeftWheelID)
        self.frontRightWheel = wpilib.Talon(robotmap.portsList.frontRightWheelID)
        self.rearLeftWheel = wpilib.Talon(robotmap.portsList.rearLeftWheelID)
        self.rearRightWheel = wpilib.Talon(robotmap.portsList.rearRightWheelID)

        self.robotDrive = wpilib.RobotDrive(self.frontLeftWheel, self.rearLeftWheel, self.frontRightWheel, self.rearLeftWheel)

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())

    def set(self, x, y, z, gyro=0):
        if robotmap.stateList.fourWheelDrive:
            self.robotDrive.arcadeDrive(y, x)
        else:
            self.robotDrive.mecanumDrive_Cartesian(x, y, z, gyro)
