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
        startIntakeButton.whenPressed(RunIntake(robotmap.speedsList.intakeSpeed))
        stopIntakeButton = JoystickButton(self.joystick, robotmap.buttonsList.stopIntakeID)
        stopIntakeButton.whenPressed(intake.getCurrentCommand().end)

        startOutputButton = JoystickButton(self.joystick, robotmap.buttonsList.startOutputID)
        startOutputButton.whenPressed(StartOutput(robotmap.speedsList.outputSpeed))
        stopOutputButton = JoystickButton(self.joystick, robotmap.buttonsList.stopOutputID)
        stopOutputButton.whenPressed(output.getCurrentCommand().end)

        openGearDoorButton = JoystickButton(self.joystick, robotmap.buttonsList.openGearID)
        openGearDoorButton.whenPressed(RunGearOutake(robotmap.positionList.openPosition))
        closeGearDoorButton = JoystickButton(self.joystick, robotmap.buttonsList.closeGearID)
        closeGearDoorButton.whenPressed(RunGearOutake(robotmap.positionList.closePosition))

        startRopeIntakeButton = JoystickButton(self.joystick, robotmap.buttonsList.startRopeID)
        startRopeIntakeButton.whenPressed(RunRopeIntake(robotmap.speedsList.intakeSpeed))
        stopRopeIntakeButton = JoystickButton(self.joystick, robotmap.buttonsList.stopRopeID)
        stopRopeIntakeButton.whenPressed(ropeintake.getCurrentCommand().end)

    def getXAxis(self):.
        return self.joystick.getX()

    def getYAxis(self):
        return self.joystick.getY()

    def getZAxis(self):
        return self.joystick.getZ()
