from wpilib.command import Command

import subsystems
import operatorinput as oi

import robotmap

import math


class Rotate(Command):

    def __init__(self, degrees):
        super().__init__('Rotate')

        self.requires(subsystems.drivetrain)

        self.degrees = degrees

    def initialize(self):
        subsystems.drivetrain.frEncoder.reset()
        subsystems.drivetrain.flEncoder.reset()
        subsystems.drivetrain.brEncoder.reset()
        subsystems.drivetrain.blEncoder.reset()

        print("Rotate Initialized")
        subsystems.drivetrain.printEncoderValues()

    def execute(self):
        if self.degrees >= 0:
            subsystems.drivetrain.set(.4, 0, 0, 0)
        else:
            subsystems.drivetrain.set(-.4, 0, 0, 0)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if self.degrees >= 0:
            leftDist = subsystems.drivetrain.flEncoder.getDistance()
            rightDist = -1 * subsystems.drivetrain.frEncoder.getDistance()
        else:
            leftDist = -1 * subsystems.drivetrain.flEncoder.getDistance()
            rightDist = subsystems.drivetrain.frEncoder.getDistance()

        circ = robotmap.auto.wheelBaseDiameter * math.pi

        avgDeg = (((leftDist / circ) * 360) + ((rightDist / circ) * 360)) / 2

        if avgDeg >= math.fabs(self.degrees):
            print("Rotate finished")
            subsystems.drivetrain.printEncoderValues()
            return True
        else:
            return False
