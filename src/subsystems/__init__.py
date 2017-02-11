from .drivetrain import Drivetrain
from .fueloutake import FuelOutake
from .gear import Gear
from .rope import Rope

drivetrain = None
fuelOutake = None
gear = None
rope = None


def init():

    global drivetrain, fuelOutake, gear, rope

    drivetrain = Drivetrain()
    fuelOutake = FuelOutake()
    gear = Gear()
    rope = Rope()
