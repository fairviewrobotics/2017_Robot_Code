import wpilib
from commandbased import CommandBasedRobot

import subsystems

from commands.autonomous.autonomous import Autonomous
from commands.gear.closegear import CloseGear

import operatorinput

import robotmap

class Robot(CommandBasedRobot):
    """Robot program base framework.

    Overridden init and periodic methods are called at appropriate
    times automatically.
    """

    def robotInit(self):
        """Robot initiializer. Initializes things such as all of the subsystems
        and operator input objects.

        Runs once during startup.
        """
        subsystems.init()
        operatorinput.init()

        self.autonomous = Autonomous()

        print("Initialized robot")

    def autonomousInit(self):
        """Prepares the code for the autonomous period.
        """
        CloseGear().start()

        self.autonomous.start()

    def teleopInit(self):
        """Prepares the code for the tele-operated period.

        Runs once when remote control is activated
        """
        self.autonomous.cancel()
        
        print("Remote control initialized.")

if __name__ == '__main__':
    wpilib.run(Robot)
