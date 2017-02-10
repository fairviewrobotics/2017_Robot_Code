from wpilib.command import InstantCommand
import subsystems
import robotmap


class StopIntake(InstantCommand):

    def __init__(self):
        super().__init__('Stop Intake')
        self.requires(subsystems.intake)

    def initialize(self):
        subsystems.intake.set(0)

    def isFinished(self):
        return super().isFinished()
