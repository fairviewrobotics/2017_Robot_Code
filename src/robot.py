import wpilib
import subsystems
from commandbased import CommandBasedRobot
import operatorinput
from commands import runintake
import robotmap


class Robot(CommandBasedRobot):

    """
    Runs once during startup, initializes robot.
    """

    def robotInit(self):
        subsystems.init()
        print("Initialized robot.")
        operatorinput.init()

    """
    Runs once when remote control is activated, initializes teleop.
    """

    def teleopInit(self):
        runintake.RunIntake(robotmap.speedsList.intakeSpeed).start()
        print("Remote control initialized.")

if __name__ == '__main__':
    wpilib.run(Robot)
