from wpilib.command import Command
import subsystems
import robotmap


class RunOutput(Command):

    def __init__(self, speed):
        super().__init__('Run Output')
        self.requires(subsystems.output)
        self.speed = speed

    def execute(self):
        subsystems.output.set(self.speed)

    def isFinished(self):
        super().isFinished()

    def interrupted(self):
        subsystems.output.set(0)

    # When finished, the output will just start coasting
    def end(self):
        subsystems.output.set(0)
