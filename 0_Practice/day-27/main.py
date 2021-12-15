import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height= 300)
window.config(padx=20, pady=20)

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
    print(input.get())

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click Me", command=button_clicked)
button2.grid(column=3, row=0)

#Entry

input = tkinter.Entry(width=20)
input.grid(column=4, row=2)









window.mainloop()