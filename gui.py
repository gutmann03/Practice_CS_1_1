from tkinter import *
from tkinter.ttk import LabeledScale
from tkinter import filedialog as fd 
import graphBuilder as gb
import mathGraphBuilder as mgb

# def saveGrapg(img):
#     def innerFunc():
#         #contents = PhotoImage(file=img)
#         new_file = fd.askdirectory(title='save graph')
#         print(new_file)
#         # save(str(new_file) + '.png', 'PNG')
#         # if new_file:
#         #     new_file.write(contents)
#         #     new_file.close()
#     return innerFunc

    

root = Tk()
root.title('Graph builder')
root.geometry('810x485+100+100')
root.resizable(False, False)

iconGr = PhotoImage(file='icons/iconGr.png')
root.iconphoto(False, iconGr)

# -1.139 -- 1.139
lblStartPos = Label(text='start value', font=24)
lblStartPos.place(x=15, y=0)
startPosEl = Entry(root, font=24, width=6)
startPosEl.place(x=110, y=2)

lblSetEndPos = Label(text='end value', font=24)
lblSetEndPos.place(x=15, y=30)
endPosEl = Entry(root, font=24, width=6)
endPosEl.place(x=110, y=32)

lblSetstep = Label(text='step', font=24)
lblSetstep.place(x=15, y=60)
stepEl = Entry(root, font=24, width=6)
stepEl.place(x=110, y=62)

def buildGrapg():
    outputString = ''

    startPos, ok = mgb.getFloatNum(startPosEl.get())
    if not ok:
        outputString += 'incorrect symbols in\nstart value\n\n'
    
    endPos, ok = mgb.getFloatNum(endPosEl.get())
    if not ok:
        outputString += 'incorrect symbols in\nend value\n\n'
        
    step, ok = mgb.getFloatNum(stepEl.get())
    if not ok:
        outputString += 'incorrect symbols in\nstep value\n\n'

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
btnBuildGrapg.place(x=5, y=90)

btnSaveGraph = Button(text='save', font=24)#, command=saveGrapg('tempPic.png'))
btnSaveGraph.place(x=62, y=90)

btnInfo = Button(text='info', font=24)
btnInfo.place(x=120, y=90)

lblScreen = Label(font='Times 13', justify='left', fg='#FF0000')
lblScreen.place(x=5, y=130)

grahpImg = PhotoImage(file='startPic.png').subsample(3, 3)
lblGrapg = Label(image=grahpImg)
lblGrapg.place(x=170, y=0)

root.rowconfigure(7, minsize=60)

root.mainloop()