from wpilib.command import Command
import subsystems
import robotmap
import operatorinput as oi
import math


class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.driveTrain)

    def execute(self):
        x = oi.joystick.getX()
        y = oi.joystick.getY()
        z = oi.joystick.getZ()

        if x >= 0:
            xValue = robotmap.speedsList.minimumWheelRotation + (1 - robotmap.speedsList.minimumWheelRotation)*(x ** 3)
        else:
            xValue = -1 * robotmap.speedsList.minimumWheelRotation + (1 - robotmap.speedsList.minimumWheelRotation)*(x ** 3)

        if y >= 0:
            yValue = robotmap.speedsList.minimumWheelRotation + (1 - robotmap.speedsList.minimumWheelRotation)*(y ** 3)
        else:
            yValue = -1 * robotmap.speedsList.minimumWheelRotation + (1 - robotmap.speedsList.minimumWheelRotation)*(y ** 3)

        subsystems.driveTrain.set(xValue, yValue, z, 0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        return super().isFinished()
