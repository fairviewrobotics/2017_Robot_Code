from wpilib.command import Command
import subsystem
import robotmap

class RunGearOutake(Command):

    def __init__(self):
        super().__init__('Gear Outake')
        self.requires(subsystems.gearoutake)
