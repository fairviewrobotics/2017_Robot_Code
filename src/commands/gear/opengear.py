import wpilib
from wpilib.command import Command
import subsystems
import robotmap


class OpenGear(Command):

    def __init__(self):
        super().__init__('Open Gear Door')
        self.requires(subsystems.gear)

    def initialize(self):
        subsystems.gear.open()

    def execute(self):
        pass

    def end(self):
        pass

    def isFinished(self):
        return super().isFinished()
