import tkinter as tk
def details():
     label2.config(text="Name: Mohammed Farhan Ahmed\nAge: 19\nCountry: India")

window=tk.Tk()
window.title("Details")

label=tk.Label(window,text="Click the below button ")
label.pack()                                #places label inside window
                        
button=tk.Button(window,text="Display details",command=details)
button.pack()                               #places button inside window

label2=tk.Label(window,text="")
label2.pack()

window.mainloop()                           #starts the tkinter loop