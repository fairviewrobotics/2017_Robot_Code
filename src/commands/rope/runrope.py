from wpilib.command import Command
import robotmap
import subsystems


class RunRope(Command):

    def __init__(self, speed):
        super().__init__('Run Rope')
        self.requires(subsystems.rope)
        self.speed = speed

    def execute(self):
        subsystems.rope.set(self.speed)

    def isFinished(self):
        return super().isFinished()

    def end(self):
        subsystems.rope.set(0)
