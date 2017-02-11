from types import SimpleNamespace

stateList = SimpleNamespace()
stateList.fourWheelDrive = True  # False if Mecanum

portsList = SimpleNamespace()

portsList.stickID = 0

portsList.rearRightWheelID = 0
portsList.frontLeftWheelID = 1
portsList.rearLeftWheelID = 2
portsList.frontRightWheelID = 3

portsList.ropeMotorID = 4

portsList.gearDoorID = 5

portsList.fuelOutakeMotorID = 6

buttonsAndAxesList = SimpleNamespace()

buttonsAndAxesList.startFuelOutakeID = 7
buttonsAndAxesList.stopFuelOutakeID = 8

buttonsAndAxesList.openGearID = 6
buttonsAndAxesList.closeGearID = 5

buttonsAndAxesList.rope60PercentID = 3
buttonsAndAxesList.rope100PercentID = 4

buttonsAndAxesList.ropeAxis = 4

positionList = SimpleNamespace()
positionList.closeGearDoorPosition = 0.0
positionList.openGearDoorPosition = 1.0

speedsList = SimpleNamespace()
speedsList.ropeSpeed = 0.9
speedsList.fuelOutakeSpeed = 0.9
speedsList.deadZoneRadius = 0.1
speedsList.minimumWheelRotation = 0.2

encoders = SimpleNamespace()
encoders.fr = [0, 1]
encoders.fl = [2, 3]
encoders.br = [4, 5]
encoders.bl = [6, 7]

auto = SimpleNamespace()
auto.initialDrive = 0
