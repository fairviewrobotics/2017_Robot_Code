from wpilib.command.commandgroup import CommandGroup

from .move import Move
from .rotate import Rotate
from .drivewaitcommand import DriveWaitCommand

from commands.gear.opengear import OpenGear

import robotmap


class AutonomousLeft(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous Program (Turn Left)')

        self.addSequential(Move(robotmap.auto.initialDrive))
        self.addSequential(Rotate(-60))
        self.addSequential(Move(robotmap.auto.stageTwoDrive))
        self.addSequential(OpenGear())
        self.addSequential(DriveWaitCommand(1))
        self.addSequential(Move(robotmap.auto.stageThreeDrive))
