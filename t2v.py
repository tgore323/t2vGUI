import gtts
import PySimpleGUI as sg
import os

layout = [
	[sg.Text('Create voice files by selecting a text file with each desired item on a new line. Ensure there are no blank lines at the end of the file.')],
	# [sg.Text('Enter text to convert to speech:')],
	[[sg.Text("Choose a file: "), sg.FileBrowse(key="-IN-")]],
	[sg.Button('OK'), sg.Button('QUIT')]
]

window = sg.Window('txt2voice by KE6QBV', layout, margins=(300,50))

while True:
	event, values = window.read()
	if event == 'OK':
		print(values['-IN-'])
	elif event == 'QUIT' or event == sg.WIN_CLOSED:
		break



window.close()