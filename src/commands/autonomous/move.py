from wpilib.command import Command
import subsystems
import robotmap
import operatorinput as oi
import math


class Move(Command):

    def __init__(self, dist):
        super().__init__('Move')

        self.requires(subsystems.driveTrain)

        subsystems.driveTrain.frEncoder.reset()
        subsystems.driveTrain.flEncoder.reset()
        subsystems.driveTrain.brEncoder.reset()
        subsystems.driveTrain.blEncoder.reset()

        self.dist = dist

    def execute(self):
        subsystems.driveTrain.set(0.6, 0, 0, 0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        if subsystems.driveTrain.frEncoder.getDistance() > self.dist - 5:
            return True
        else:
            return False
