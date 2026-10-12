import PySimpleGUI as sg
import time as time
import random as random

UPPER_TIME_LIMIT = 7
LOWER_TIME_LIMIT = 3

global oneTimer
oneTimer = False
global greenTime
greenTime = False
sg.theme("Dark Blue")
reactCanvas =[sg.Canvas(size=(500, 300), key='-CANVAS-', background_color='red')]
reactionlayout = [reactCanvas,
                  [sg.Text("This is the reaction time test")],
                  [sg.Button("Start Test")]
                  ]
reactionwindow = sg.Window('Canvas Click Test', reactionlayout, size=(500,500),  finalize=True)
sg_canvas = reactionwindow['-CANVAS-'].TKCanvas

global startTime
startTime = 0

def reactionTimeTest():
    global oneTimer
    global greenTime
    global startTime
    if oneTimer == True:
        reactionwindow['-CANVAS-'].update(background_color = "red")

        randTimer = random.randint(LOWER_TIME_LIMIT, UPPER_TIME_LIMIT)
        time.sleep(randTimer)

        reactionwindow['-CANVAS-'].update(background_color = "green")
        startTime = time.time()
        greenTime = True
        oneTimer = False


def reactionGreenClick(event):
    global greenTime
    global startTime
    if greenTime == True:
        print("Clicked after ",time.time() - startTime, "seconds")
        reactionwindow["-CANVAS-"].update(background_color = "red")

sg_canvas.bind("<Button-1>", reactionGreenClick)

while True:
    event, values = reactionwindow.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Start Test":
        oneTimer = True
        greenTime = False
        reactionTimeTest()
reactionwindow.close()
