import PySimpleGUI as sg
import eng_cn
import os
# Turn off padding in order to get a really tight looking layout.

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))
sg.theme('DarkBrown4') # give our window a spiffy set of colors
mode = 'EN_CN'
layout = [[sg.Text('Translation', size=(40, 1))],
          [sg.Output(size=(150, 20), font=('Calibri 15'))],
          [sg.Multiline(size=(20, 2), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[1], sg.BLUES[1]), bind_return_key=True),
           sg.Push(),
           sg.Button('MODE',  button_color=(sg.YELLOWS[1], sg.BLUES[0])),
           sg.Push(),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))],
           [sg.Push()],
           [sg.HorizontalSeparator()],
           [sg.Push()],
           [    sg.Push(),
                sg.Text(key='-TEXT-',size=(40, 1))], # text mode = EN_CN
           ]


window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), 
                   use_default_focus=False, 
                   auto_size_text=False,
                   auto_size_buttons=True,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1))


MODE_MAP = {
    'EN_CN': 'CN_PY',
    'CN_PY': 'PY_EN',
    'PY_EN': 'EN_CN',
    }
MODE_KEY = {
    'EN_CN': 'English to Chinese',
    'CN_PY': 'Chinese to Pinyin',
    'PY_EN': 'Pinyin to English',
    }
while True:     # The Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break

    if event == 'SEND':
        query = values['-QUERY-'].rstrip()
        if mode=="EN_CN":
            query= eng_cn.EN_CN(word=query)
        elif mode=="CN_PY":
            byte_string = query.encode('utf-8')
            text = byte_string.decode('utf-8')
            query= eng_cn.CN_PY(word=text)
        elif mode=="PY_EN":
            query= eng_cn.PY_EN(word=query)
        for x in query:
            print(x, flush=True)
    if event == 'MODE':
        # Get the next mode from the dictionary.
        next_mode = MODE_MAP[mode]
        # Set the current mode to the next mode.
        mode = next_mode
        window['-TEXT-'].update(MODE_KEY[mode])
window.close()