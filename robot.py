import wpilib
import subsystems
from commandbased import CommandBasedRobot

class Robot(CommandBasedRobot):

    """
    Runs once durring startup, initializes robot.
    """
    def robotInit(self):
        subsystems.init()
        print("Initialized robot.")

    """
    Runs once when remote control is activated, initializes teleop.
    """
    def teleopInit(self):
        RunIntake().start()
        print("Remote control initialized.")

if __name__ == '__main__':
    wpilib.run(Robot)
