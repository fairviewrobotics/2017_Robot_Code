from .drivetrain import DriveTrain
from .operatorinput import OperatorInput
from .intake import Intake

driveTrain = None
operatorInput = None
intake = None

def init():

    global driveTrain, operatorInput, intake

    intake = Intake()
    driveTrain = DriveTrain()
    operatorinput = OperatorInput()
