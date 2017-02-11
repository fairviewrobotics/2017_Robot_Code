import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap


class Rope(Subsystem):

    def __init__(self):
        super().__init__('Rope Mechanism')
        self.motor = wpilib.Talon(robotmap.portsList.ropeMotorID)

    def set(self, speed):
        self.motor.set(speed)
