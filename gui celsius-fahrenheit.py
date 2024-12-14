import tkinter as tk
def convert():
    celsius=float(entry.get())      #to take input inside window 
    fahrenheit=(celsius*5/9)+32
    label2.config(text=f"fahrenheit temperature :{fahrenheit}")

window=tk.Tk()
window.title("Celcius to fahrenheit")

label=tk.Label(window,text="Enter Celcius temperature")
label.pack()

entry=tk.Entry(window)              #creates a white space for input 
entry.pack()

button=tk.Button(window,text="convert",command=convert)
button.pack()

label2=tk.Label(window,text="")
label2.pack()

window.mainloop()