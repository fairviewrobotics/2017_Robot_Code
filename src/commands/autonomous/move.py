from wpilib.command import Command

import math

import subsystems

import operatorinput as oi

import robotmap


class Move(Command):

    def __init__(self, dist):
        super().__init__('Move')

        self.requires(subsystems.drivetrain)

        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        self.dist = dist

    def initialize(self):
        pass

    def execute(self):
        if self.dist >= 0:
            subsystems.drivetrain.set(0.6, 0, 0, 0)
        else:
            subsystems.drivetrain.set(-0.6, 0, 0, 0)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        avgDist = (math.fabs(subsystems.drivetrain.frEncoder.getDistance()) + math.fabs(subsystems.drivetrain.flEncoder.getDistance()) + math.fabs(subsystems.drivetrain.blEncoder.getDistance())) / 3

        if avgDist > math.fabs(self.dist) - 5:
            return True
        else:
            return False
