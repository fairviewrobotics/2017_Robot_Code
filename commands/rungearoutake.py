import wpilib
from wpilib.command import Command
import subsystems
import robotmap

class RunGearOutake(Command):

    def __init__(self, position):
        super().__init__('Gear Outake')
        self.requires(subsystems.gearoutake)
        self.position = position

    def execute(self):
        subsystems.gearoutake.set(self.position)
