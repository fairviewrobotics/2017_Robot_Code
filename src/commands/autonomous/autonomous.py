from wpilib.command.commandgroup import CommandGroup

from .move import Move

class Autonomous(CommandGroup):
    
    def __init__(self):
        super().__init__('Autonomous Program')

        self.addSequential(Move())
