import matplotlib.pyplot as plt
import mathGraphBuilder as mgb
from tkinter import filedialog as fd

class GraphBuilder:
        def __init__(self) -> None:
                self.fig = plt.figure()
        
        def buildGraph(self, startPoint:float, endPoint:float, step:float):
                xS, yUppers, yLowers = mgb.getCoordinates(startPoint, endPoint, step)
                ax = self.fig.add_subplot(111)
                ax.arrow(-2.0, 0, 4, 0, color = 'black', width = 0.01)
                ax.arrow(0, -2.5, 0, 5, color = 'black', width = 0.01)
                ax.plot(xS, yUppers, color='red')
                ax.plot(xS, yLowers, color='red')

                ax.text(1.8, -0.2, 'x', fontsize = 10)
                ax.text(0.01, 2.0, 'y', fontsize =  10)

                self.ax = ax

        def saveWithPath(self):
                path = fd.asksaveasfilename(title="save graph")
                self.fig.savefig(f"{path}", dpi=300)

        def save(self):
                self.fig.savefig("tempPic.png", dpi=300)

        def close(self):
                plt.close(self.fig)