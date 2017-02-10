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
        xAxis = oi.joystick.getX()
        yAxis = oi.joystick.getY()
        zAxis = oi.joystick.getZ()
        distance = math.sqrt(math.pow(xAxis, 2) + math.pow(yAxis, 2))
        if distance <= robotmap.speedsList.deadZoneRadius:
            xAxis = 0
            yAxis = 0
        else:
            xAxis = (xAxis - robotmap.speedsList.deadZoneRadius) / \
                (1 - robotmap.speedsList.deadZoneRadius)
            yAxis = (yAxis - robotmap.speedsList.deadZoneRadius) / \
                (1 - robotmap.speedsList.deadZoneRadius)
        subsystems.driveTrain.set(xAxis, yAxis, zAxis, 0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
        return super().isFinished()
