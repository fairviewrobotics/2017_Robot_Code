import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap


class FuelOutake(Subsystem):

    def __init__(self):
        super().__init__('Fuel Outake')
        self.motor = wpilib.Talon(robotmap.portsList.fuelOutakeMotorID)

    def set(self, speed):
        self.motor.set(speed)
