from tkinter import *
from tkinter import filedialog as fd 
import graphBuilder as gb
import mathGraphBuilder as mgb

class MyGUI:
    def __init__(self) -> None:
        self.grapher = gb.GraphBuilder()
        self.root = Toplevel()
        self.isChanged = False

        self.root.title('Graph builder')
        self.root.geometry('1230x720+50+50')
        self.root.resizable(False, False)

        iconGr = PhotoImage(file='./icons/iconGr.png')
        self.root.iconphoto(False, iconGr)

        self.lblStartPos = Label(self.root, text='start value', font='Times 16')
        self.lblStartPos.place(x=25, y=0)
        self.startPosEl = Entry(self.root, font='Times 16', width=6)
        self.startPosEl.place(x=180, y=4)

        self.lblEndPos = Label(self.root, text='end value', font='Times 16')
        self.lblEndPos.place(x=25, y=40)
        self.endPosEl = Entry(self.root, font='Times 16', width=6)
        self.endPosEl.place(x=180, y=46)

        self.lblStep = Label(self.root, text='step', font='Times 16')
        self.lblStep.place(x=25, y=80)
        self.stepEl = Entry(self.root, font='Times 16', width=6)
        self.stepEl.place(x=180, y=88)

        self.btnBuildGrapg = Button(self.root, text='build', font='Times 16', command=self.buildGrapg)
        self.btnBuildGrapg.place(x=5, y=130)

        self.btnSaveGraph = Button(self.root, text='save', font='Times 16', command=self.saveGraph)
        self.btnSaveGraph.place(x=110, y=130)

        self.btnInfo = Button(self.root, text='info', font='Times 16', command=self.info)
        self.btnInfo.place(x=200, y=130)

        self.btnQuit = Button(self.root, text='quit', fg="red", font='Times 16', command=self.quit)
        self.btnQuit.place(x=5, y=660)

        self.lblScreen = Label(self.root)
        self.lblScreen.place(x=5, y=200)

        self.startImg = PhotoImage(file='startPic.png').subsample(2, 2)
        self.lblGrapg = Label(self.root, image=self.startImg)
        self.lblGrapg.place(x=270, y=0)

    def buildGrapg(self):
        outputString = ''

        startPos, ok = mgb.getFloatNum(self.startPosEl.get())
        if not ok:
            outputString += 'incorrect symbols in\nstart value\n\n'
        
        endPos, ok = mgb.getFloatNum(self.endPosEl.get())
        if not ok:
            outputString += 'incorrect symbols in\nend value\n\n'
            
        step, ok = mgb.getFloatNum(self.stepEl.get())
        if not ok:
            outputString += 'incorrect symbols in\nstep value\n\n'

        outputString += mgb.checkStartValue(startPos)
        outputString += mgb.checkEndValue(endPos)
        outputString += mgb.checkDifferenceValue(startPos, endPos)
        outputString += mgb.checkStepValue(step)

        self.lblScreen.config(text=outputString, font='Times 16', justify='left', fg='red')
        
        if len(outputString) == 0:
            self.grapher.buildGraph(startPos, endPos, step)
            self.grapher.save()
            newGraph = PhotoImage(file='tempPic.png').subsample(2, 2)
            self.lblGrapg.config(image=newGraph)
            self.isChanged = True

    def saveGraph(self):
        if self.isChanged:
            self.grapher.saveWithPath()
            self.lblGrapg.config(image=self.startImg)
            self.isChanged = False
        else:
            outputString = 'There is nothing to save.\nBuild something first.'
            self.lblScreen.config(text=outputString, font='Times 13', justify='left', fg='magenta')

    def info(self):
        outputString = "This program builds graph\nof the equation of love.\n\nDespite the fact that\ngraph of this equation\n\
defined on the R, but\nlocated only in interval\n[-1.139, 1.139] є X,\nStatr value must be\ngreater then -1.14,\nand less then 1.14.\n\
The same but reversed\nrule for end value.\n\nStep must be positive\nfloat number.\n(recomended to take\nnumber 0.01 and less)"

        self.lblScreen.config(text=outputString, font='Times 13', justify='left', fg='blue')

    def quit(self):
        self.close()
        self.root.destroy()

    def close(self):
        self.grapher.close()
        