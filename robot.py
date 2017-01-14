import wpilib

from commandbased import CommandBasedRobot

class Robot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

    def teleopInit(self):
        StartIntake().start()
