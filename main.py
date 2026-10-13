import PySimpleGUI as sg

sg.theme("Dark Blue")
mainLayout = [[sg.Text("This is the Human Bench Mark Test")],
            [sg.Button("Tests")]
              ]
mainWindow = sg.Window('BenchmarkMain', mainLayout, size=(1000,1000), finalize=True)
