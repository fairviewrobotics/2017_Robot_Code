from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.fueloutake.runfueloutake import RunFuelOutake
from commands.fueloutake.stopfueloutake import StopFuelOutake

from commands.gear.closegear import CloseGear
from commands.gear.opengear import OpenGear

from commands.rope.runrope import RunRope
from commands.rope.stoprope import StopRope

import robotmap


joystick = None

def init():
    global joystick

    joystick = Joystick(robotmap.portsList.stickID)

    startFuelOutakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startFuelOutakeID)
    startFuelOutakeButton.whenPressed(RunFuelOutake(robotmap.speedsList.fuelOutakeSpeed))
    stopFuelOutakeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopFuelOutakeID)
    stopFuelOutakeButton.whenPressed(StopFuelOutake())

    openGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.openGearID)
    openGearDoorButton.whenPressed(
        OpenGear())
    closeGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.closeGearID)
    closeGearDoorButton.whenPressed(
        CloseGear())

    startRopeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.startRopeID)
    startRopeButton.whenPressed(
        RunRope(robotmap.speedsList.ropeSpeed))
    stopRopeButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.stopRopeID)
    stopRopeButton.whenPressed(StopRope())
