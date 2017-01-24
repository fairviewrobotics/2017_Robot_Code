class emptyList:
    pass

stateList = emptyList()
stateList.fourWheelDrive = True # False if Mecanum

portsList = emptyList()
portsList.frontLeftWheelID = 0
portsList.frontRightWheelID = 1
portsList.rearLeftWheelID = 2
portsList.rearRightWheelID = 3
portsList.intakeMotorID = 4
portsList.outputMotorID = 5
portsList.stickID = 0

buttonsList = emptyList()
buttonsList.startIntakeID = 1
buttonsList.stopIntakeID = 2
buttonsList.startOutputID = 3
buttonsList.stopOutputID = 4

speedsList = emptyList()
speedsList.intakeSpeed = 0.9
speedsList.outputSpeed = 0.9
