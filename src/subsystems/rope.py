import wpilib
from wpilib.command.subsystem import Subsystem

import robotmap


class Rope(Subsystem):
    """Subsystem for the rope mechanism.

    This is used to control the motor that spins to suck the rope in.

    Instance variables:

    - motor: The motor that spins to suck the rope in.
    """

    def __init__(self):
        """`Rope` constructor. Constructs a `Rope` object.
        """
        super().__init__('Rope Mechanism')

        self.motor = wpilib.Talon(robotmap.portsList.ropeMotorID)

    def set(self, speed):
        """Sets the rope motor's speed value.
        """
        self.motor.set(speed)
