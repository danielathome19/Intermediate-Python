""" Description: 
Calculates the MPG (rounded to the nearest 10th gal) 
of a car given its miles and gallons used. Allows the user 
to add new cars to the list of cars and calculate their MPG.
"""
import PySimpleGUI as sg
from dataclasses import dataclass


@dataclass
class Car:
    name: str
    miles: int
    gallons: float

    def mpg(self):
        return self.miles / self.gallons


def add_car():
    layout = [
        [sg.Text("Name:"), sg.Input(key='name')],
        [sg.Text("Miles:"), sg.Input(key='miles')],
        [sg.Text("Gallons:"), sg.Input(key='gallons')],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]

    form = sg.Window("Add New Car", layout, modal=True)
    event, values = form.read()
    form.close()

    if event == "Add":
        try:
            return Car(values['name'], int(values['miles']), float(values['gallons']))
        except ValueError:
            sg.popup_error("Invalid input!")
    return None


cars = {
    "1970 VW Bug": Car("1970 VW Bug", 286, 9),
    "1979 Firebird": Car("1979 Firebird", 412, 40),
    "1980 Subaru": Car("1980 Subaru", 361, 18),
    "1975 Cutlass": Car("1975 Cutlass", 161, 11)
}


def main():
    layout = [
        [sg.Text("Select Car:"), sg.Combo(list(cars), key='car', readonly=True)],
        [sg.Text("Miles Per Gallon:"), sg.Text("", key='mpg')],
        [sg.Button("Calculate"), sg.Button("Add New Car"), sg.Button("Exit")]
    ]

    window = sg.Window("MPG Calculator", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == "Calculate" and values["car"] is not None:
            window['mpg'].update(f"{cars[values['car']].mpg():.1f} mpg")

        if event == "Add New Car":
            car = add_car()
            if car:
                cars[car.name] = car
                window['car'].update(values=list(cars), value=car.name)
                window['mpg'].update('')
    
    window.close()
    pass


if __name__ == "__main__":
    main()
