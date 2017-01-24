import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap

class Output(Subsystem):

    def __init__(self):
        super().__init__('Drive Train')
        self.motor = wpilib.Talon(robotmap.portsList.outputMotorID)

    def set(self, speed):
        self.motor.set(speed)
