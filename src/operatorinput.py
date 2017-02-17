from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.fueloutake.runfueloutake import RunFuelOutake
from commands.fueloutake.stopfueloutake import StopFuelOutake

from commands.gear.closegear import CloseGear
from commands.gear.opengear import OpenGear

import robotmap

joystick = None

def init():
    global joystick

    joystick = Joystick(robotmap.portsList.stickID)

    openGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.openGearID)
    openGearDoorButton.whenPressed(
        OpenGear())
    closeGearDoorButton = JoystickButton(
        joystick, robotmap.buttonsAndAxesList.closeGearID)
    closeGearDoorButton.whenPressed(
        CloseGear())
