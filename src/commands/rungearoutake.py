import wpilib
from wpilib.command import Command
import subsystems
import robotmap


class RunGearOutake(Command):

    def __init__(self, position):
        super().__init__('Gear Outake')
        self.requires(subsystems.gearOutake)
        self.position = position

    def execute(self):
        subsystems.gearOutake.set(self.position)

    def interrupted(self):
        pass

    def isFinished(self):
        # super().isFinished()
        return False
