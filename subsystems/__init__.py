from .drivetrain import DriveTrain
from .operatorinput import OperatorInput
from .intake import Intake

driveTrain = None
operatorInput = None
intake = None

def init():

    global driveTrain, operatorInput, intake

    driveTrain = DriveTrain()
    operatorinput = OperatorInput()
    intake = Intake()
