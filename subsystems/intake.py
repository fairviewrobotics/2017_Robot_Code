import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap


class Intake(Subsystem):

    def __init__(self):
        super().__init__('Ball Intake')
        self.motor = wpilib.Talon(robotmap.portsList.intakeMotorID)

    def set(self, speed):
        self.motor.set(speed)
