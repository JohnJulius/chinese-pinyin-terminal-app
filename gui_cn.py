import PySimpleGUI as sg

# Create an empty dictionary
dictionary = {}

# Define the layout of the GUI
layout = [
    [sg.Text("Word:"), sg.InputText(key="word")],
    [sg.Text("Definition:"), sg.InputText(key="definition")],
    [sg.Button("Add Word"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("Pinyin App", layout)

# Event loop to process "Add Word" and "Exit" events
while True:
    event, values = window.read()
    if event == "Add Word":
        word = values["word"]
        definition = values["definition"]
        dictionary[word] = definition
        sg.popup(f"Added {word} to the dictionary!")
        window["word"].update("")
        window["definition"].update("")
    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

# Close the window
window.close()
