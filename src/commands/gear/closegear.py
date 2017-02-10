import wpilib
from wpilib.command import Command
import subsystems
import robotmap


class CloseGear(Command):

    def __init__(self):
        super().__init__('Close Gear Door')
        self.requires(subsystems.gear)

    def initialize(self):
        subsystems.gear.close()

    def execute(self):
        pass

    def end(self):
        pass

    def isFinished(self):
        return super().isFinished()
