import wpilib
import subsystems
from commandbased import CommandBasedRobot

class Robot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

    def teleopInit(self):
        RunIntake().start()

if __name__ == '__main__':
    wpilib.run(Robot)
