import wpilib
from wpilib.command.subsystem import Subsystem

import robotmap


class Gear(Subsystem):
    """Subsystem for the gear mechanism.

    This is used to control the servo that opens and closes the gear mechanism
    door.

    Instance variables:

    - servo: The servo that opens and closes the gear mechanism door.
    """

    def __init__(self):
        """`Gear` constructor. Constructs a `Gear` object.
        """
        super().__init__('Gear Outake')

        self.servo = wpilib.Servo(robotmap.portsList.gearDoorID)

    def open(self):
        """Opens the gear mechanism door.
        """
        self.servo.set(robotmap.positionList.openGearDoorPosition)

    def close(self):
        """Closes the gear mechanism door.
        """
        self.servo.set(robotmap.positionList.closeGearDoorPosition)
