import wpilib
from wpilib.command.subsystem import Subsystem

from commands.followjoystick import FollowJoystick

import subsystems

import robotmap


class Drivetrain(Subsystem):
    """Subsystem for the drivetrain.

    This is used to control all of the wheels.

    Instance variables:

    - robotDrive: The object used to set motor values for the drivetrain.
    """

    def __init__(self):
        """`Drivetrain` constructor. Constructs an `Drivetrain` object.
        """
        super().__init__('Drivetrain')

        frontLeftWheel = wpilib.Talon(robotmap.portsList.frontLeftWheelID)
        frontRightWheel = wpilib.Talon(
            robotmap.portsList.frontRightWheelID)
        backLeftWheel = wpilib.Talon(robotmap.portsList.rearLeftWheelID)
        backRightWheel = wpilib.Talon(robotmap.portsList.rearRightWheelID)

        self.robotDrive = wpilib.RobotDrive(
            self.frontLeftWheel,
            self.backLeftWheel,
            self.frontRightWheel,
            self.backRightWheel)

        self.robotDrive.setInvertedMotor(
            wpilib.RobotDrive.MotorType.kRearLeft, True)
        self.robotDrive.setInvertedMotor(
            wpilib.RobotDrive.MotorType.kFrontLeft, True)

        self.frEncoder = wpilib.Encoder(*robotmap.encoders.fr)
        self.frEncoder.setDistancePerPulse(robotmap.encoders.distancePerPulse)

        self.flEncoder = wpilib.Encoder(*robotmap.encoders.fl)
        self.flEncoder.setDistancePerPulse(robotmap.encoders.distancePerPulse)

        self.brEncoder = wpilib.Encoder(*robotmap.encoders.br)
        self.brEncoder.setDistancePerPulse(robotmap.encoders.distancePerPulse)

        self.blEncoder = wpilib.Encoder(*robotmap.encoders.bl)
        self.blEncoder.setDistancePerPulse(robotmap.encoders.distancePerPulse)

        print("Drivetrain object created")

    def initDefaultCommand(self):
        """Sets the default command of this subsystem to the `FollowJoystick`
        command.

        This will run when nothing else is running on the `Drivetrain` subsytem.
        """
        self.setDefaultCommand(FollowJoystick())
        print("Set the default command of the `Drivetrain` to  `FollowJoystick`.")

    def set(self, x, y, z, gyro=0):
        """Sets motor values via `robotDrive` based joystick x, y, and z axis
        values and whether we are using mecanum or four wheel drive.
        """
        if robotmap.stateList.fourWheelDrive:
            self.robotDrive.arcadeDrive(y, x)
        else:
            self.robotDrive.mecanumDrive_Cartesian(x, y, z, gyro)
