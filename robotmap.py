class EmptyList:
    pass

stateList = EmptyList()
stateList.fourWheelDrive = True # False if Mecanum

portsList = EmptyList()
portsList.frontLeftWheelID = 0
portsList.frontRightWheelID = 1
portsList.rearLeftWheelID = 2
portsList.rearRightWheelID = 3
portsList.intakeMotorID = 4
portsList.outputMotorID = 5
portsList.stickID = 0

buttonsList = EmptyList()
buttonsList.startIntakeID = 1
buttonsList.stopIntakeID = 2
buttonsList.startOutputID = 3
buttonsList.stopOutputID = 4

speedsList = EmptyList()
speedsList.intakeSpeed = 0.9
speedsList.outputSpeed = 0.9
