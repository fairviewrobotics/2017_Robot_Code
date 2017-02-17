from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from .move import Move
from .rotate import Rotate

from commands.gear.opengear import OpenGear

import robotmap


class AutonomousStraight(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous Program (Straight)')

        self.addSequential(Move(robotmap.auto.straightDrive))
        self.addSequential(OpenGear())
        self.addSequential(WaitCommand(1))
        self.addSequential(Move(robotmap.auto.stageThreeDrive))
