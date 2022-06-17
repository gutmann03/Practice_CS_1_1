import string

def getLeftPart(x:float) -> float:
    return pow(abs(x), (2/3))

def getRightPart(x:float) -> float:
    return pow((pow(abs(x), (4/3)) + 4 * (1 - pow(abs(x), 2))), 0.5)

def getUpper(x:float) -> float:
    return 0.5 * (getLeftPart(x) + getRightPart(x))

def getLower(x:float) -> float:
    return 0.5 * (getLeftPart(x) - getRightPart(x))

def getCoordinates(startPoint:float, endPoint:float, step:float) -> tuple[list, list, list]:
    xS, yUppers, yLowers = [], [], []
    x = startPoint
    while x <= endPoint:
        xS.append(x)

        yUppers.append(getUpper(x))

        yLowers.append(getLower(x))
        x += step
    
    xS.append(endPoint)
    yUppers.append(getUpper(endPoint))
    yLowers.append(getLower(endPoint))
    return xS, yUppers, yLowers

def checkStartValue(startValue:float) -> string:
    if(startValue < -1.139):
        return 'start value must be\nnot less then -1.139.\n\n'
    return ''

def checkEndValue(endValue:float) -> string:
    if(endValue > 1.139):
        return 'end value must be\nnot bigger then 1.139.\n\n'
    return ''

def checkDifferenceValue(startValue:float, endValue:float) -> string:
    if(startValue > endValue):
        return 'start value must be\nless then end value.\n\n'
    return ''

def checkStepValue(stepValue:float) -> string:
    if(stepValue <= 0.0):
        return 'step must be\nbigger then 0.\n\n'
    return ''

def getFloatNum(value:string) -> tuple[float, bool]:
    try:
        outValue = float(value)
        return outValue, True
    except Exception:
        return 0.1, False