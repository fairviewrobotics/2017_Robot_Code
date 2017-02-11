from .drivetrain import DriveTrain
from .output import Output
from .gear import Gear
from .ropeintake import RopeIntake

driveTrain = None
output = None
gear = None
ropeIntake = None


def init():

    global driveTrain, output, gear, ropeIntake

    driveTrain = DriveTrain()
    output = Output()
    gear = Gear()
    ropeIntake = RopeIntake()
