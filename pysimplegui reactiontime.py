import PySimpleGUI as sg
import time as time
import random as random

global oneTimer
oneTimer = False
global greenTime
greenTime = False 
sg.theme("Dark Blue") #createst the window layout plus canvas element for the test
reactCanvas =[sg.Canvas(size=(500, 300), key='-CANVAS-', background_color='red')]
reactionlayout = [[sg.Text("This is the reaction time test")],
                  [sg.Text("-"*200)],
                  reactCanvas,
                  [sg.Text("-"*200)],
                  [sg.Button("Start Test")]
                  ]
reactionwindow = sg.Window('Canvas Click Test', reactionlayout, size=(500,500),  finalize=True)
sg_canvas = reactionwindow['-CANVAS-'].TKCanvas

global startTime
startTime = 0

def reactionTimeTest(): #The function to register the button to a timer that starts the test
    global oneTimer
    global greenTime
    global startTime
    if oneTimer == True:
        reactionwindow['-CANVAS-'].update(background_color = "red")
        randTimer = random.randint(3,7)
        print("Timer of ",randTimer," seconds.")
        time.sleep(randTimer)
        reactionwindow['-CANVAS-'].update(background_color = "green")
        startTime = time.time()
        greenTime = True
        oneTimer = False
        print("Updated variables")


def reactionGreenClick(event): #The function to register when the canvas is clicked after the timer counts down
    global greenTime
    global startTime
    if greenTime == True:
        greenTime == False
        print("Clicked after ",(time.time() - startTime)*10000, "milliseconds")
        reactionwindow["-CANVAS-"].update(background_color = "red")
        
    else:
        print("greenTime not set")

sg_canvas.bind("<Button-1>", reactionGreenClick)




while True: #Stays open constantly allowing for buttons and closing the window to be available constantly
    event, values = reactionwindow.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Start Test":
        oneTimer = True
        greenTime = False
        reactionTimeTest()
reactionwindow.close()

    

    
