import wpilib
from wpilib.command.subsystem import Subsystem

import robotmap


class FuelOutake(Subsystem):
    """Subsystem for the fuel outake.

    This is used to control the motor that sucks the fuel in.

    Instance variables:

    - motor: The motor that sucks the fuel in.
    """

    def __init__(self):
        """`FuelOutake` constructor. Constructs a `FuelOutake` object.
        """
        super().__init__('Fuel Outake')

        self.motor = wpilib.Talon(robotmap.portsList.fuelOutakeMotorID)

    def set(self, speed):
        """Sets the fuel intake motor speed value.
        """
        self.motor.set(speed)
