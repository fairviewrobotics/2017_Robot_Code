from wpilib.command import Command

import subsystems

import robotmap

class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.driveTrain)

    def execute(self):
        subsystems.driveTrain.set(subsystems.operatorInput.getX(), subsystems.operatorInput.getY(), subsystems.operatorInput.getZ(), 0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        super().isFinished()
