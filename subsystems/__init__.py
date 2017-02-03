from .drivetrain import DriveTrain
from .intake import Intake
from .output import Output
from .gearoutake import GearOutake
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
    gearOutake = GearOutake()
    ropeIntake = RopeIntake()
