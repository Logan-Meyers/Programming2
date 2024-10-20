# https://www.youtube.com/watch?v=ibf5cx221hk
import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onClosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.showMessage)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='Your mom- message', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 16), height=5)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.checkState = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.checkState)
        self.check.pack(padx=10, pady=10)

        self.clrButton = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clrButton.pack()

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 18), command=self.showMessage)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.root.mainloop()
    
    def showMessage(self):
        # print(self.checkState.get())
        if (self.checkState.get() == 0):
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if (event.state == 4) and (event.keysym == "Return"):
            self.showMessage()
    
    def onClosing(self):
        if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
            # if yes; true:
            self.root.destroy()
        else:
            # else no; false:
            pass
    
    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()