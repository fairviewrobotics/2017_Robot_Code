from wpilib.command import Command
import subsystems
import robotmap
import operatorinput as oi

class FollowJoystick(Command):

    def __init__(self):
        super().__init__('Follow Joystick')
        self.requires(subsystems.driveTrain)

    def execute(self):
        subsystems.driveTrain.set(oi.joystick.getX(), oi.joystick.getY(), oi.joystick.getZ(), 0)

    def end(self):
        subsystems.driveTrain.set(0, 0, 0, 0)

    def isFinished(self):
       #super().isFinished()
       return False
