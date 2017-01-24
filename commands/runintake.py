from wpilib.command import Command
import subsystems
import robotmap

class RunIntake(Command):

    def __init__(self, speed):
        super().__init__('Run Intake')
        self.requires(subsystems.intake)
        self.speed = speed

    def execute(self):
        subsystems.intake.set(self.speed)

    def isFinished(self):
        super().isFinished()

    #When finished, the intake will just start coasting
    def end(self):
        subsystems.intake.set(0)
