import numpy as np
import matplotlib.pyplot as plt
import mathGraphBuilder as mgb

# startPoint = -1
# endPoint = 0.7
# step = 0.006
def buildGrapg(startPoint:float, endPoint:float, step:float):
        xS, yUppers, yLowers = mgb.getCoordinates(startPoint, endPoint, step)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.arrow(-2.0, 0, 4, 0,
                color = 'black',
                width = 0.01)

        ax.arrow(0, -2.5, 0, 5,
                color = 'black',
                width = 0.01)

        ax.plot(xS, yUppers, color='red')
        ax.plot(xS, yLowers, color='red')

        ax.text(1.8, -0.2, 'x',
                fontsize = 10)

        ax.text(0.01, 2.0, 'y',
                fontsize = 10)

        plt.savefig('tempPic.png', dpi=300)
        # plt.show()