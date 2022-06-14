import string


def getCoordinates(startPoint:float, endPoint:float, step:float) -> tuple[list, list, list]:
    xS, yUppers, yLowers = [], [], []
    x = startPoint
    while x <= endPoint:
        xS.append(x)

        yUpper = 0.5*(pow(abs(x), (2/3)) + pow((pow(abs(x), (4/3)) + 4 * (1 - pow(abs(x), 2))), 0.5))
        yUppers.append(yUpper)

        yLower = 0.5*(pow(abs(x), (2/3)) - pow((pow(abs(x), (4/3)) + 4 * (1 - pow(abs(x), 2))), 0.5))
        yLowers.append(yLower)
        x += step
    
    return xS, yUppers, yLowers

def checkStartValue(startValue:float) -> string:
    if(startValue < -1.139):
        return 'start value must be\nnot less then -1.139.\n\n'
    return ''

def checkEndValue(endValue:float) -> string:
    if(endValue > 1.139):
        return 'end value must be\nnot greater then 1.139.\n\n'
    return ''

def checkDifferenceValue(startValue:float, endValue:float) -> string:
    if(startValue > endValue):
        return 'start value must be\nless then end value.\n\n'
    return ''

def checkStepValue(stepValue:float) -> string:
    if(stepValue <= 0.0):
        return 'step must be\ngreater then 0.\n\n'
    return ''

def getFloatNum(value:string) -> tuple[float, bool]:
    try:
        outValue = float(value)
        return outValue, True
    except:
        return 0.1, False