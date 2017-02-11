import wpilib
import subsystems
from commandbased import CommandBasedRobot

from commands.autonomous.autonomous import Autonomous
from commands.gear.closegear import CloseGear

import operatorinput

import robotmap

class Robot(CommandBasedRobot):

    """
    Runs once during startup, initializes robot.
    """

    def robotInit(self):
        subsystems.init()
        print("Initialized robot.")
        operatorinput.init()

        self.autonomous = Autonomous()

    def autonomousInit(self):
        CloseGear().start()
        
        self.autonomous.start()

    """
    Runs once when remote control is activated, initializes teleop.
    """
    def teleopInit(self):
        self.autonomous.cancel()
        print("Remote control initialized.")

if __name__ == '__main__':
    wpilib.run(Robot)
