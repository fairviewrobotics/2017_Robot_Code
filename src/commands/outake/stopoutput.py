from wpilib.command import InstantCommand
import subsystems
import robotmap


class StopOutput(InstantCommand):

    def __init__(self):
        super().__init__('Stop Output')
        self.requires(subsystems.output)

    def initialize(self):
        subsystems.output.set(0)

    def isFinished(self):
        return super().isFinished()
