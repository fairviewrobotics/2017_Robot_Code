from wpilib.command import Command

import subsystems
import operatorinput as oi

import robotmap

import math

class Rotate(Command):

    def __init__(self, degrees):
        super().__init__('Rotate')
        self.requires(subsystems.driveTrain)

        subsystems.driveTrain.frEncoder.reset()
        subsystems.driveTrain.flEncoder.reset()
        subsystems.driveTrain.brEncoder.reset()
        subsystems.driveTrain.blEncoder.reset()

        self.degrees = degrees

    def initialize(self):
        if self.degrees >= 0:
            subsystems.driveTrain.rearLeftWheel.set(.6)
            subsystems.driveTrain.rearRightWheel.set(-.6)
        else:
            subsystems.driveTrain.rearLeftWheel.set(-.6)
            subsystems.driveTrain.rearRightWheel.set(.6)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        if self.degrees >= 0:
            leftDist = subsystems.driveTrain.backLeft.getDistance()
            rightDist = -1 * subsystems.driveTrain.backRight.getDistance()
        else:
            leftDist = -1 * subsystems.driveTrain.backLeft.getDistance()
            rightDist = subsystems.driveTrain.backRight.getDistance()

        circ = robotmap.auto.wheelBaseDiameter * math.pi

        avgDeg = (((leftDist / circ) * 360) + ((rightDist / circ) * 360)) / 2

        if avgDeg >= self.degrees:
            return True
        else:
            return False
