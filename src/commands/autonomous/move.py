from wpilib.command import Command
import subsystems
import robotmap
import operatorinput as oi
import math


class Move(Command):

    def __init__(self, dist):
        super().__init__('Move')

        self.requires(subsystems.drivetrain)

        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        self.dist = dist

    def execute(self):
        subsystems.drivetrain.set(0.6, 0, 0, 0)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if subsystems.drivetrain.frEncoder.getDistance() > self.dist - 5:
            return True
        else:
            return False
