import wpilib
from commandbased import CommandBasedRobot

import subsystems

from commands.autonomous.autonomousleft import AutonomousLeft
from commands.autonomous.autonomousright import AutonomousRight
from commands.autonomous.autonomousstraight import AutonomousStraight

from commands.autonomous.move import Move
from commands.autonomous.rotate import Rotate

from commands.gear.closegear import CloseGear

import operatorinput

import robotmap

class Robot(CommandBasedRobot):
    """Robot program base framework.

    Overridden init and periodic methods are called at appropriate
    times automatically.
    """

    def robotInit(self):
        """Robot initiializer. Initializes things such as all of the subsystems
        and operator input objects.

        Runs once during startup.
        """
        subsystems.init()
        operatorinput.init()

        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.addDefault("Straight Autonomous", AutonomousStraight())
        self.autoChooser.addObject("Left Autonomous", AutonomousLeft())
        self.autoChooser.addObject("Right Autonomous", AutonomousRight())
        self.autoChooser.addObject("Straigh 1 foot", Move(12))
        self.autoChooser.addObject("Rotate 90 degrees", Rotate(90))

        wpilib.SmartDashboard.putData("Autonomous Mode Chooser", self.autoChooser)

        self.autoProgram = AutonomousLeft()

        wpilib.SmartDashboard.putData('Scheduler', wpilib.command.Scheduler.getInstance())

        wpilib.SmartDashboard.putData('Drivetrain', subsystems.drivetrain)
        wpilib.SmartDashboard.putData('Fuel Outake', subsystems.fuelOutake)
        wpilib.SmartDashboard.putData('Gear Mech', subsystems.gear)
        wpilib.SmartDashboard.putData('Rope Mech', subsystems.rope)

        print("Initialized robot")

    def autonomousInit(self):
        """Prepares the code for the autonomous period.
        """
        CloseGear().start()

        # self.autoProgram = self.autoChooser.getSelected()
        self.autoProgram.start()

        print("Autonomous initialized")

    def autonomousPeriodic(self):
        """Periodic code for the autonomous period.

        Called every 20ms or so.
        """
        wpilib.command.Scheduler.getInstance().run()

    def teleopInit(self):
        """Prepares the code for the tele-operated period.

        Runs once when remote control is activated
        """
        self.autoProgram.cancel()

        print("Tele-op initialized.")

    def teleopPeriodic(self):
        """Periodic code for the tele-operated period.

        Called every 20ms or so.
        """
        wpilib.command.Scheduler.getInstance().run()

if __name__ == '__main__':
    wpilib.run(Robot)
