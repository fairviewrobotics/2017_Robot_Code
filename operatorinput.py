from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.runintake import RunIntake
from commands.rungearoutake import RunGearOutake
from commands.runoutput import RunOutput
from commands.runropeintake import RunRopeIntake

from commands.stopintake import StopIntake
from commands.stopoutput import StopOutput
from commands.stopropeintake import StopRopeIntake

import robotmap


joystick = None


def init():
    global joystick

    joystick = Joystick(robotmap.portsList.stickID)

    startIntakeButton = JoystickButton(
        joystick, robotmap.buttonsList.startIntakeID)
    startIntakeButton.whenPressed(RunIntake(robotmap.speedsList.intakeSpeed))
    stopIntakeButton = JoystickButton(
        joystick, robotmap.buttonsList.stopIntakeID)
    stopIntakeButton.whenPressed(StopIntake())

    startOutputButton = JoystickButton(
        joystick, robotmap.buttonsList.startOutputID)
    startOutputButton.whenPressed(RunOutput(robotmap.speedsList.outputSpeed))
    stopOutputButton = JoystickButton(
        joystick, robotmap.buttonsList.stopOutputID)
    stopOutputButton.whenPressed(StopOutput())

    openGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsList.openGearID)
    openGearDoorButton.whenPressed(
        RunGearOutake(
            robotmap.positionList.openPosition))
    closeGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsList.closeGearID)
    closeGearDoorButton.whenPressed(
        RunGearOutake(robotmap.positionList.closePosition))

    startRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsList.startRopeID)
    startRopeIntakeButton.whenPressed(
        RunRopeIntake(robotmap.speedsList.intakeSpeed))
    stopRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsList.stopRopeID)
    stopRopeIntakeButton.whenPressed(StopRopeIntake())
