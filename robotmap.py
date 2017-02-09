from types import SimpleNamespace

stateList = SimpleNamespace()
stateList.fourWheelDrive = True  # False if Mecanum

portsList = SimpleNamespace()
portsList.frontLeftWheelID = 0
portsList.frontRightWheelID = 1
portsList.rearLeftWheelID = 2
portsList.rearRightWheelID = 3
portsList.intakeMotorID = 4
portsList.outputMotorID = 5
portsList.stickID = 0
portsList.gearDoorID = 6
portsList.ropeMotorID = 7

buttonsList = SimpleNamespace()
buttonsList.startIntakeID = 1
buttonsList.stopIntakeID = 2
buttonsList.startOutputID = 3
buttonsList.stopOutputID = 4
buttonsList.openGearID = 5
buttonsList.closeGearID = 6
buttonsList.startRopeID = 7
buttonsList.stopRopeID = 8

positionList = SimpleNamespace()
positionList.closePosition = 0.0
positionList.openPosition = 0.8

speedsList = SimpleNamespace()
speedsList.intakeSpeed = 0.9
speedsList.outputSpeed = 0.9
speedsList.deadZoneRadius = 0.1
