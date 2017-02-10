import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap


class GearOutake(Subsystem):

    def __init__(self):
        super().__init__('Gear Outake')
        self.servo = wpilib.Servo(robotmap.portsList.gearDoorID)

    def set(self, position):
        self.servo.set(position)
