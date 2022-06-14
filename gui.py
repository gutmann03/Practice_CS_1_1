from tkinter import *
from tkinter.ttk import LabeledScale
import graphBuilder as gb
import mathGraphBuilder as mgb

root = Tk()
root.title('Graph builder')
root.geometry('800x500+50+50')
root.minsize(800, 500)

iconGr = PhotoImage(file='icons/iconGr.png')
root.iconphoto(False, iconGr)

# -1.139 -- 1.139
lblStartPos = Label(text='start value', font=24)
lblStartPos.grid(row=0, column=0, columnspan=2)
startPosEl = Entry(root, font=24, width=6)
startPosEl.grid(row=1, column=1, columnspan=2)

lblSetEndPos = Label(text='end value', font=24)
lblSetEndPos.grid(row=2, column=0, columnspan=2)
endPosEl = Entry(root, font=24, width=6)
endPosEl.grid(row=3, column=1, columnspan=2)

lblSetstep = Label(text='step', font=24)
lblSetstep.grid(row=4, column=0, columnspan=2)
stepEl = Entry(root, font=24, width=6)
stepEl.grid(row=5, column=1, columnspan=2)

def buildGrapg():
    outputString = ''

    startPos, ok = mgb.getFloatNum(startPosEl.get())
    if not ok:
        outputString += 'incorrect symbols in start value\n'
    
    endPos, ok = mgb.getFloatNum(endPosEl.get())
    if not ok:
        outputString += 'incorrect symbols in end value\n'
        
    step, ok = mgb.getFloatNum(stepEl.get())
    if not ok:
        outputString += 'incorrect symbols in step value\n'

    outputString += mgb.checkStartValue(startPos)
    outputString += mgb.checkEndValue(endPos)
    outputString += mgb.checkDifferenceValue(startPos, endPos)
    outputString += mgb.checkStepValue(step)

    lblScreen.config(text=outputString)
    
    if len(outputString) == 0:
        gb.buildGrapg(startPos, endPos, step)
        newGraph = PhotoImage(file='tempPic.png').subsample(3, 3)
        lblGrapg.config(image=newGraph)
        # lblScreen.config(text='')

btnBuildGrapg = Button(text='build', font=24, command=buildGrapg)
btnBuildGrapg.grid(row=6, column=0)

btnSaveGraph = Button(text='save', font=24)
btnSaveGraph.grid(row=6, column=1)

btnInfo = Button(text='info', font=24)
btnInfo.grid(row=6 , column=2)

lblScreen = Label(text='asdasd', font=24, fg='#FF0000')
lblScreen.grid(row=7, column=0, columnspan=3)

grahpImg = PhotoImage(file='startPic.png').subsample(3, 3)
lblGrapg = Label(image=grahpImg)
lblGrapg.grid(row=0, column=3, rowspan=8)

root.rowconfigure(7, minsize=60)

root.mainloop()