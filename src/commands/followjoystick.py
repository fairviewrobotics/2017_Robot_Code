from wpilib.command import Command

import subsystems

import operatorinput as oi

import robotmap


class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.drivetrain)
        self.requires(subsystems.rope)

    def execute(self):
        x = oi.joystick.getX()
        y = oi.joystick.getY()
        z = oi.joystick.getZ()

        if x >= 0:
            xValue = robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (x ** 3)
        else:
            xValue = -1 * robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (x ** 3)

        if y >= 0:
            yValue = robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (y ** 3)
        else:
            yValue = -1 * robotmap.speedsList.minimumWheelRotation + \
                (1 - robotmap.speedsList.minimumWheelRotation) * (y ** 3)

        subsystems.drivetrain.set(xValue, yValue, z, 0)

        if oi.joystick.getRawButton(
                robotmap.buttonsAndAxesList.rope60PercentID):
            subsystems.rope.set(0.6)
        elif oi.joystick.getRawButton(robotmap.buttonsAndAxesList.rope100PercentID):
            subsystems.rope.set(1)
        else:
            value = oi.joystick.getRawAxis(
                robotmap.buttonsAndAxesList.ropeAxis) ** 3
            subsystems.rope.set(value)

        if oi.joystick.getRawButton(
                robotmap.buttonsAndAxesList.fuelOutake60PercentID):
            subsystems.fuelOutake.set(0.6)
        elif oi.joystick.getRawButton(robotmap.buttonsAndAxesList.fuelOutake100PercentID):
            subsystems.fuelOutake.set(1)
        else:
            value = oi.joystick.getRawAxis(
                robotmap.buttonsAndAxesList.fuelOutakeAxis) ** 3
            subsystems.fuelOutake.set(value)

        if oi.joystick.getRawButton(
            robotmap.buttonsAndAxesList.inverseDirectionID):
            if subsystems.drivetrain.inverted:
                subsystems.drivetrain.inverted = False
            else:
                subsystems.drivetrain.inverted = True

    def end(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def isFinished(self):
        return super().isFinished()
