from wpilib.command import InstantCommand
import robotmap
import subsystems


class StopRope(InstantCommand):

    def __init__(self):
        super().__init__('Stop Rope')
        self.requires(subsystems.rope)

    def initialize(self):
        subsystems.rope.set(0)

    def isFinished(self):
        return super().isFinished()
