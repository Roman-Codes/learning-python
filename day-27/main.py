from tkinter import *

window = Tk()
window.title("Miles/km converter")

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="km")
kilometer_label.grid(row=2, column=1)

def convert():
    miles = miles_input.get()
    km = float(miles) * 1.609
    kilometer_result_label.config(text=f"{km}")


calculate_button = Button(text="Convert", command=convert)
calculate_button.grid(row=2, column=1)

mainloop()