import PySimpleGUI as sg
import tkinter as tk

sg.theme("Dark blue")
def reactionTimeTest():
    
    reactionTestLayout = [[sg.Text("This is the reaction time test")],
                          [sg.Text("-"*200)],
                          [sg.Canvas(background_color="red", size =(500,300), key ='-REACTIONCANVAS-')],
                          [sg.Text("-"*200)]
                         ]
    global reactionTimeTestWindow 
    reactionTimeTestWindow = sg.Window("ReactionTimeTest", reactionTestLayout, size=(500,500), finalize=True)
    global tk_canvas
    while True:
        event, values = reactionTimeTestWindow.Read()
        if event == sg.WINDOW_CLOSED:
            break
    reactionTimeTestWindow.close()


def canvasclick(event):
    print(f"clicked at coordinates: X={event.x}, Y={event.y}")
    tk_canvas = reactionTimeTestWindow["-REACTIONCANVAS-"].TKCanvas
    tk_canvas.bind("<Button1>", canvasclick)

reactionTimeTest()
