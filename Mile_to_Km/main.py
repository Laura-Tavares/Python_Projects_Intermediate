from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx = 20, pady = 20)
#window.minsize(width=500, height=300)

miles_input = Entry(width=5)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

equal_label = Label(text="is equal to")
equal_label.grid(column = 0, row = 1)

result = Label(text="0")
result.grid(column = 1, row = 1)

km_label = Label(text="Kilometers")
km_label.grid(column = 2, row = 1)

calculate_button = Button(text="Calculate", command= miles_to_km)
calculate_button.grid(column = 1, row = 2)


window.mainloop()
