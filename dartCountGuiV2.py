# libraries
from tkinter import *
from PIL import ImageTk, Image
import math

#globals
totalScore = 0
scoreKeep =[]

#functions
def scoreFunction(a, r):
    number = 0
    multiplier = 1

    #positive x
    if -9 < a < 9:
        number = 6
    elif 9 <= a < 27:
        number = 13
    elif 27 <= a < 45:
        number = 4
    elif 45 <= a < 63:
        number = 18
    elif 63 <= a < 81:
        number = 1
    elif 81 <= a < 99:
        number = 20
    elif 99 <= a < 117:
        number = 5
    elif 117 <= a < 135:
        number = 12
    elif 135 <= a < 153:
        number = 9
    elif 153 <= a < 171:
        number = 14

    #negative x
    elif -27 < a <= -9:
        number = 10
    elif -45 < a <= -27:
        number = 15
    elif -63 < a <= -45:
        number = 2
    elif -81 < a <= -63:
        number = 17
    elif -99 < a <= -81:
        number = 3
    elif -117 < a <= -99:
        number = 19
    elif -135 < a <= 117:
        number = 7
    elif -153 < a <= -135:
        number = 16
    elif -171 < a <= -153:
        number = 8
    elif -171 >= a or a >= 171:
        number = 11

    #ring 
    if r > 245:
        multiplier = 0
    elif r > 225:
        multiplier = 2
    elif r < 155 and r > 135:
        multiplier = 3
    elif r < 14:
        number = 25
        multiplier = 2
    elif r < 25:
        number = 25
        multiplier = 1
    
    #returning score
    return number, multiplier
    
def angleRadius(xd, yd):
    xd = -306 + xd 
    yd = 306 - yd

    #angle
    try:
        angle = math.atan(yd/xd) / math.pi *180
        if xd < 0 and yd > 0:
            angle = 180 + angle
        elif xd < 0 and yd < 0:
            angle = -180 + angle
    except:
        if yd == 0:
            if xd > 0:
                angle = 0
            elif xd < 0:
                angle = 180
            elif xd == 0:
                radius = 0
                angle = 0
        elif yd > 0:
            angle = 90
        elif yd < 0:
            angle = -90
    #radius
    radius = math.sqrt(xd**2 + yd**2)

    #getting the score
    score, multi = scoreFunction(angle, radius)
    printScore(score, multi)
    
def enter(e):
    x = e.x
    y = e.y
    angleRadius(x, y)

def printScore(sc, mp):
    calculatedScore = sc * mp
    listOfGlobals = globals()

    #total score
    listOfGlobals['totalScore'] += calculatedScore
    totalString = "Total: " + str(listOfGlobals['totalScore'])
    lbl_total['text'] = totalString

    #latest input
    LatInString = ""
    if sc == 25 and mp == 1:
        LatInString = LatInString + "BULL"
    elif sc == 25 and mp == 2:
        LatInString = LatInString + "BULLSEYE"
    elif mp == 1:
        LatInString = LatInString + "S" + str(sc)
    elif mp == 2:
        LatInString = LatInString + "D" + str(sc)
    elif mp == 3:
        LatInString = LatInString + "T" + str(sc)
    lbl_input['text'] = "Latest score: " + LatInString

    #score keeping
    listOfGlobals['scoreKeep'].append(LatInString)
    scoreKeepString = "Score: \n"
    for string in listOfGlobals['scoreKeep']:
        scoreKeepString = scoreKeepString + string + "\n"
    lbl_score['text'] = scoreKeepString
    print(sc, mp)
    
#GUI
window = Tk()

window.geometry("612x700")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

#Image
frame = Frame(window, width=612, height=612)
frame.grid(row=0, column=0)
frame.place(anchor='n', relx=0.5)

img = ImageTk.PhotoImage(Image.open("dartBoard2.jpg"))

lbl_image = Label(frame, image = img)
lbl_image.pack()

#output
window.bind('<Return>', enter)

frm_output = Frame(window)
frm_output.place(y=612)

lbl_input = Label(frm_output, text="Latest input: ")
lbl_score = Label(frm_output, text="Score: " )
lbl_total = Label(frm_output, text="Total: ")

lbl_input.grid(row=1, column=0)
lbl_total.grid(row=2, column=0)
lbl_score.grid(row=3, column=0)

window.mainloop()
