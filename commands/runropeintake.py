from wpilib.command import Command
import robotmap
import subsystems

class RunRopeIntake(Command)

    def __init__(self):
        super().__init__('Run Rope Intake')
        self.requires(subsystems.ropeintake)
        self.speed = speed

    def execute(self):
        subsystems.ropeintake.set(self.speed)

    def isFinished(self):
        super().isFinished()

    def end(self):
        subsystems.ropeintake.set(0)
