from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from .move import Move
from .rotate import Rotate

from commands.gear.opengear import OpenGear

import robotmap


class AutonomousRight(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous Program (Turn Right)')

        self.addSequential(Move(robotmap.auto.initialDrive))
        self.addSequential(Rotate(60))
        self.addSequential(Move(robotmap.auto.stageTwoDrive))
        self.addSequential(OpenGear())
        self.addSequential(WaitCommand(1))
        self.addSequential(Move(robotmap.auto.stageThreeDrive))
