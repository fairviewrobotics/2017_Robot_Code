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
        if self.degrees >= 0:
            subsystems.drivetrain.rearLeftWheel.set(.6)
            subsystems.drivetrain.rearRightWheel.set(-.6)
        else:
            subsystems.drivetrain.rearLeftWheel.set(-.6)
            subsystems.drivetrain.rearRightWheel.set(.6)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if self.degrees >= 0:
            leftDist = subsystems.drivetrain.backLeft.getDistance()
            rightDist = -1 * subsystems.drivetrain.backRight.getDistance()
        else:
            leftDist = -1 * subsystems.drivetrain.backLeft.getDistance()
            rightDist = subsystems.drivetrain.backRight.getDistance()

        circ = robotmap.auto.wheelBaseDiameter * math.pi

        avgDeg = (((leftDist / circ) * 360) + ((rightDist / circ) * 360)) / 2

        if avgDeg >= math.fabs(self.degrees):
            return True
        else:
            return False
