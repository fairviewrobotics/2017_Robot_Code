from wpilib.command import Command

import subsystems

import robotmap

class RunFuelOutake(Command):

    def __init__(self, speed):
        super().__init__('Run Fuel Outake')
        self.requires(subsystems.fuelOutake)
        self.speed = speed

    def execute(self):
        subsystems.fuelOutake.set(self.speed)

    def isFinished(self):
        return super().isFinished()

    def interrupted(self):
        subsystems.fuelOutake.set(0)

    # When finished, the output will just start coasting
    def end(self):
        subsystems.fuelOutake.set(0)
