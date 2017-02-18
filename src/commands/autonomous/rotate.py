from wpilib.command import Command

import subsystems
import operatorinput as oi

import robotmap

import math


class Rotate(Command):

    def __init__(self, degrees):
        super().__init__('Rotate')

        self.requires(subsystems.drivetrain)

        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        self.degrees = degrees

    def initialize(self):
        pass

    def execute(self):
        if self.degrees >= 0:
            subsystems.drivetrain.set(.4, 0, 0, 0)
        else:
            subsystems.drivetrain.set(-.4, 0, 0, 0)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if self.degrees >= 0:
            leftDist = subsystems.drivetrain.blEncoder.getDistance()
            # rightDist = -1 * subsystems.drivetrain.brEncoder.getDistance()
        else:
            leftDist = -1 * subsystems.drivetrain.blEncoder.getDistance()
            # rightDist = subsystems.drivetrain.brEncoder.getDistance()

        circ = robotmap.auto.wheelBaseDiameter * math.pi

        # avgDeg = (((leftDist / circ) * 360) + ((rightDist / circ) * 360)) / 2
        avgDeg = (leftDist / circ) * 360

        if avgDeg >= math.fabs(self.degrees):
            return True
        else:
            return False
