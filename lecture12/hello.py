import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name:"), sg.Input(key="-NAME-", size=(20, 1))],
    [sg.Button("Submit"), sg.Button("Exit")],
    [sg.Text("", key="-OUTPUT-")]
]

window = sg.Window("Hello", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Submit":
        name = values["-NAME-"]
        window["-OUTPUT-"].update(f"Hello, {name}!")

window.close()
