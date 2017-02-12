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
        if self.dist >= 0:
            subsystems.drivetrain.set(0.6, 0, 0, 0)
        else:
            subsystems.drivetrain.set(-0.6, 0, 0, 0)

    def execute(self):
        pass

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if math.fabs(
                subsystems.drivetrain.frEncoder.getDistance()) > math.fabs(
                self.dist) - 5:
            return True
        else:
            return False
