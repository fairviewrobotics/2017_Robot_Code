import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap


class Gear(Subsystem):

    def __init__(self):
        super().__init__('Gear Outake')
        self.servo = wpilib.Servo(robotmap.portsList.gearDoorID)

    def open(self):
        self.servo.set(robotmap.positionList.openGearDoorPosition)

    def close(self):
        self.servo.set(robotmap.positionList.closeGearDoorPosition)
