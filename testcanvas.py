import PySimpleGUI as sg
import time as time
import random as random


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

def reactionTimeTest(event):
    global oneTimer
    reactionwindow['-CANVAS-'].update(background_color = "red")
    if oneTimer == True:
        randTimer = random.randint(3,7)
        print("Timer of ",randTimer," seconds.")
        time.sleep(randTimer)
        reactionwindow['-CANVAS-'].update(background_color = "green")
        greenTime = True
        oneTimer = False
   
    

    
def reactionGreenClick(event):
    global greenTime
    print("space")
    if greenTime == True:
        startTime = time.time()
        print("Clicked after ",time.time() - startTime, "seconds")
        reactionwindow["-CANVAS-"].update(bacground_color = "red")

sg_canvas.bind("<Button-1>", reactionTimeTest)
sg_canvas.bind("<Button-1>", reactionGreenClick)




while True:
    event, values = reactionwindow.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Start Test":
        oneTimer = True     
        greenTime = False
reactionwindow.close()
