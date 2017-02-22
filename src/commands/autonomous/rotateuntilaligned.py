from wpilib.command import Command

import subsystems
import operatorinput as oi

import robotmap

import math

from networktables import NetworkTables

class RotateUntilAligned(Command):

    def __init__(self, degrees):
        super().__init__('RotateUntilAligned')

        self.requires(subsystems.drivetrain)

        self.degrees = degrees

        self.nt = NetworkTables.getTable("camera")

    def initialize(self):
      pass

    def execute(self):
        if nt.getNumber('offset') < 0
            subsystems.drivetrain.set(.5, 0, 0, 0)
        else:
            subsystems.drivetrain.set(-.5, 0, 0, 0)

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        if abs(nt.getNumber('offset')) < 2:
          return True
        else:
          return False
