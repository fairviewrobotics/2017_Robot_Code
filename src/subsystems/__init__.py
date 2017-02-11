from .drivetrain import DriveTrain
from .fueloutake import FuelOutake
from .gear import Gear
from .rope import Rope

driveTrain = None
fuelOutake = None
gear = None
rope = None

def init():

    global driveTrain, fuelOutake, gear, rope

    driveTrain = DriveTrain()
    fuelOutake = FuelOutake()
    gear = Gear()
    rope = Rope()
