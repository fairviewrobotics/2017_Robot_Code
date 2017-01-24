import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap

class Output(Subsystem):

    def __init__(self):
        super().__init__('Ball Output')
        self.motor = wpilib.Talon(robotmap.portsList.outputMotorID)

    def set(self, speed):
        self.motor.set(speed)
