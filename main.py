import PySimpleGUI as sg

sg.theme("Dark Blue") #creating the main file in order to link all the tests to.
mainLayout = [[sg.Text("This is the Human Bench Mark Test")],
            [sg.Button("Tests")]
              ]
mainWindow = sg.Window('BenchmarkMain', mainLayout, size=(1000,1000), finalize=True)
