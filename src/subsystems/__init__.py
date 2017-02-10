from .drivetrain import DriveTrain
from .intake import Intake
from .output import Output
from .gear import Gear
from .ropeintake import RopeIntake

driveTrain = None
intake = None
output = None
gear = None
ropeIntake = None


def init():

    global driveTrain, intake, output, gear, ropeIntake

    intake = Intake()
    driveTrain = DriveTrain()
    output = Output()
    gear = Gear()
    ropeIntake = RopeIntake()
