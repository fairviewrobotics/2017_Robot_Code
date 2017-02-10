from wpilib.command import Command
import robotmap
import subsystems


class RunRopeIntake(Command):

    def __init__(self, speed):
        super().__init__('Run Rope Intake')
        self.requires(subsystems.ropeIntake)
        self.speed = speed

    def execute(self):
        subsystems.ropeIntake.set(self.speed)

    def isFinished(self):
        return super().isFinished()

    def end(self):
        subsystems.ropeIntake.set(0)
