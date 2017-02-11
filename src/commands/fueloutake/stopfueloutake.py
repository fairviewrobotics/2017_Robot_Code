from wpilib.command import Command
import subsystems
import robotmap


class StopFuelOutake(Command):

    def __init__(self):
        super().__init__('Stop Fuel Outake')
        self.requires(subsystems.fuelOutake)

    def initialize(self):
        subsystems.fuelOutake.set(0)

    def isFinished(self):
        return super().isFinished()
