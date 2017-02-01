import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap

class RopeIntake(Subsystem)

    def __init__(self):
        super().__init__('Rope Intake')
        self.motor = wpilib.Talon(robotmap.portsList.ropeMotorID)

    def set(self, speed):
        self.motor.set(speed)
