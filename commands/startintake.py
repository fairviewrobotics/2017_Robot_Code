from wpilib.command import InstantCommand

import subsystems

import robotmap

class StartIntake(InstantCommand):

    def __init__(self):
        super().__init__('Start Intake')
        self.requires(subsystems.intake)

    def initialize(self):
        subsystems.intake.set(0.9)

    def isFinished(self):
        super().isFinished()
