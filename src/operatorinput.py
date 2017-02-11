from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.outake.runoutput import RunOutput

from commands.gear.closegear import CloseGear
from commands.gear.opengear import OpenGear

from commands.rope.runropeintake import RunRopeIntake

from commands.outake.stopoutput import StopOutput
from commands.rope.stopropeintake import StopRopeIntake

import robotmap


joystick = None

def init():
    global joystick

    joystick = Joystick(robotmap.portsList.stickID)

    startOutputButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startOutputID)
    startOutputButton.whenPressed(RunOutput(robotmap.speedsList.outputSpeed))
    stopOutputButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopOutputID)
    stopOutputButton.whenPressed(StopOutput())

    openGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.openGearID)
    openGearDoorButton.whenPressed(
        OpenGear())
    closeGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.closeGearID)
    closeGearDoorButton.whenPressed(
        CloseGear())

    startRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startRopeID)
    startRopeIntakeButton.whenPressed(
        RunRopeIntake(robotmap.speedsList.intakeSpeed))
    stopRopeIntakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopRopeID)
    stopRopeIntakeButton.whenPressed(StopRopeIntake())
