import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=25, pady=50)

def calculate_km():
    km_label.config(text=int(miles_input.get())*1.60934)






#Label

my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)


#Miles entry

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)


#Km value Label

km_label = tkinter.Label(text=0)
km_label.grid(column=1, row=1)

#Calculate button

calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

#Miles label

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0)

#Km label

km_label2 = tkinter.Label(text="km")
km_label2.grid(column=2,row=1)

















window.mainloop()