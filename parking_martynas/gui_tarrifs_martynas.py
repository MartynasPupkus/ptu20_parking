import PySimpleGUI as sg
import sqlite3
from parking_db import connection, cursor


def get_tarrif_list(connection: sqlite)

def tariffs(main_window: sg.Window):
    main_window.hide

    layout = [
        [sg.Listbox()]
    ]
    window = sg.Window('Tariffs || PTU20')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

    main_window.un_hide()