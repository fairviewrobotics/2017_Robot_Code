from wpilib.command import InstantCommand
import robotmap
import subsystems


class StopRopeIntake(InstantCommand):

    def __init__(self):
        super().__init__('Stop Rope Intake')
        self.requires(subsystems.ropeIntake)

    def initialize(self):
        subsystems.ropeIntake.set(0)

    def isFinished(self):
        return super().isFinished()
