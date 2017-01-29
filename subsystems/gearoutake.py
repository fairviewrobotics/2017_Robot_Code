import wpilib
from wpilib.Servo import Servo
from wpilib.command.subsystem import Subsystem
import robotmap

class GearOutake(Subsystem)

	def __init__(self):
		super().__init__('Gear Outake')
		self.servo = wpilib.Servo(robotmap.port.gearDoorID)
		position = 0.0

	def set(self, position):
		self.servo.set(position)
