import PySimpleGUI as sg

## tariff_list (list/create/delete)
## cars_list (list/create/delete)
## arrival 
    ###(choose/create car; 
    ### create parking entry with datetime.now() as arrival time)
## departure 
    ###(choose from cars without departure, 
    ### update parking entry with datetime.now() as departure time, 
    ###calculate total_price)
## reports
    ### find parking bills by specific car
    ### total parking revenue by between dates with list
## main window

main_layout = [
    [
    sg.Button('Tariffs', key='-TARIFFS-', size=10),
    sg.Button('Cars', key='-CARS-', size=10)],

    [sg.Button('Arrival', key ='-ARRIVAL-', size=10),
    sg.Button('Departure', key = '-DEPARTURE-', size=10)],

    [sg.Button('Reports', key = '-REPORTS-', size=10)
    ]
]


main_window = sg.Window('Parking PTU20', main_layout, font ='sans-serif 20', element_justification='center', element_padding=10)

while True:
    event, values = main_window.read()
    if event == sg.WIN_CLOSED:
        break 