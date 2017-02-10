from .drivetrain import DriveTrain
from .intake import Intake
from .output import Output
from .gear import Gear
from .ropeintake import RopeIntake

driveTrain = None
intake = None
output = None
gearOutake = None
ropeIntake = None


def init():

    global driveTrain, intake, output, gearOutake, ropeIntake

    intake = Intake()
    driveTrain = DriveTrain()
    output = Output()
    gearOutake = Gear()
    ropeIntake = RopeIntake()
