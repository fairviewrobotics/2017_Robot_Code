import wpilib

import subsystems

class DriveWaitCommand(wpilib.command.TimedCommand):

    def __init__(self, seconds):
        super().__init__('Drive Wait Command', seconds)

    def initialize(self):
        pass

    def execute(self):
        subsystems.drivetrain.set(0, 0, 0, 0)

    def end(self):
        pass
