class StateList:
    pass

stateList = StateList()

stateList.fourWheelDrive = True # False if Mecanum

class PortsList:
    pass

portsList = PortsList()

portsList.frontLeftWheelID = 0
portsList.frontRightWheelID = 1
portsList.rearLeftWheelID = 2
portsList.rearRightWheelID = 3

portsList.intakeMotorID = 4

portsList.stickID = 0

class ButtonsList:
    pass

buttonsList = ButtonsList()

buttonsList.startIntakeID = 1
buttonsList.stopIntakeID = 2
