import wpilib
from wpilib.command.subsystem import Subsystem
from commands.followjoystick import FollowJoystick
import robotmap


class DriveTrain(Subsystem):

    """
        Initializes wheels using robotmap's portlist.
    """

    def __init__(self):
        super().__init__('Drive Train')

        self.frontLeftWheel = wpilib.Talon(robotmap.portsList.frontLeftWheelID)
        self.frontRightWheel = wpilib.Talon(
            robotmap.portsList.frontRightWheelID)
        self.rearLeftWheel = wpilib.Talon(robotmap.portsList.rearLeftWheelID)
        self.rearRightWheel = wpilib.Talon(robotmap.portsList.rearRightWheelID)

        self.robotDrive = wpilib.RobotDrive(
            self.frontLeftWheel,
            self.rearLeftWheel,
            self.frontRightWheel,
            self.rearLeftWheel)

        self.robotDrive.setInvertedMotor(wpilib.RobotDrive.MotorType.kRearLeft, True)
        self.robotDrive.setInvertedMotor(wpilib.RobotDrive.MotorType.kFrontRight, True)
        self.robotDrive.setInvertedMotor(wpilib.RobotDrive.MotorType.kFrontLeft, True)

        print("Wheels initialized with portlist.")

        self.frEncoder = wpilib.Encoder(*robotmap.encoders.fr)
        self.flEncoder = wpilib.Encoder(*robotmap.encoders.fl)
        self.brEncoder = wpilib.Encoder(*robotmap.encoders.br)
        self.blEncoder = wpilib.Encoder(*robotmap.encoders.bl)

    """
        Sets default command of subsystem to be the follow joystick class.
        This will run when nothing else is running.
    """

    def initDefaultCommand(self):
        self.setDefaultCommand(FollowJoystick())
        print("The default command of drivetrain is now the joystick class.")

    """
        arcadeDrive uses moveValue as y and rotateValue as x
        mecanumDrive_Cartesian uses x as the speed in x, y as the speed in y,
        z as the rotation, and doesn't really care about gyro.
    """

    def set(self, x, y, z, gyro=0):
        if robotmap.stateList.fourWheelDrive:
            self.robotDrive.arcadeDrive(y, x)
            print("Robot is using arcadeDrive.")
        else:
            self.robotDrive.mecanumDrive_Cartesian(x, y, z, gyro)
            print("Robot is using mecanumDrive_Cartesian")
