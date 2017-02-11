from .drivetrain import DriveTrain
from .fueloutake import FuelOutake
from .gear import Gear
from .ropeintake import RopeIntake

driveTrain = None
fuelOutake = None
gear = None
ropeIntake = None


def init():

    global driveTrain, fuelOutake, gear, ropeIntake

    driveTrain = DriveTrain()
    fuelOutake = FuelOutake()
    gear = Gear()
    ropeIntake = RopeIntake()
