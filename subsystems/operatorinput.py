from wpilib.command.subsystem import Subsystem

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.startintake import StartIntake

import robotmap

class OperatorInput(Subsystem):

    def __init__(self):
        super().__init__('Operator Input')

        self.joystick = Joystick(robotmap.portsList.stickID)

        startIntakeButton = JoystickButton(self.joystick, robotmap.buttonsList.startIntakeID)
        startIntakeButton.whenPressed(StartIntake())

        stopIntakeButton = JoystickButton(self.joystick, robotmap.buttonsList.stopIntakeID)
        # stopIntakeButton.whenPressed(StopIntake())

    def getXAxis(self):
        return self.joystick.getX()

    def getYAxis(self):
        return self.joystick.getY()

    def getZAxis(self):
        return self.joystick.getZ()
