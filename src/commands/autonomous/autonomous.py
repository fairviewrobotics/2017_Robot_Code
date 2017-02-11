from wpilib.command.commandgroup import CommandGroup

from .move import Move
from .rotate import Rotate

class Autonomous(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(Move())
        self.addSequential(Rotate(-60))
