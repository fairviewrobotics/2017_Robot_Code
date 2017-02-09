from wpilib.command import Command
import subsystems
import robotmap
import operatorinput as oi
import math

class Move(Command):

    def __init__(self):
        super().__init__('Move')
        self.requires(subsystems.driveTrain)
        driveTrain.frEncoder.reset()
        driveTrain.flEncoder.reset()
        driveTrain.brEncoder.reset()
        driveTrain.blEncoder.reset()

    def execute(self):
        subsystems.driveTrain.set(0.75,0.75,1,0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        if driveTrain.frEncoder.getDistance() > robotmap.auto.initalDrive - 5:
          return True
        else:
          return False
