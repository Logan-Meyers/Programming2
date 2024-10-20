import tkinter as tk
import config
import authenticator as auther
from tkinter import messagebox as mbx


class LoginPage:
    def __init__(self, autoShow=True):
        # main root window
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.root.config(bg=config.Colors.DarkPurple)

        # entry variables
        self.enteredUsername = tk.StringVar()
        self.enteredPassword = tk.StringVar()

        # function to call when logging in
        self.loginFunc = lambda: None

        # widgets making
        self.titleFrame = tk.Frame(self.root)
        self.titleLabel = tk.Label(self.titleFrame, text="Welcome!", font=config.Fonts.Title)
        self.subTitleLabel = tk.Label(self.titleFrame, text="Please log in:", font=config.Fonts.SubTitle)

        self.loginFrame = tk.Frame(self.root)
        self.userLabel = tk.Label(self.loginFrame, text="Username/Email:", font=config.Fonts.Normal)
        self.userEntBox = tk.Entry(self.loginFrame, textvariable=self.enteredUsername, font=config.Fonts.Normal)
        self.userEntBox.bind("<KeyPress>", self.shortcut)
        self.passLabel = tk.Label(self.loginFrame, text="Password:", font=config.Fonts.Normal)
        self.passEntBox = tk.Entry(self.loginFrame, textvariable=self.enteredPassword, font=config.Fonts.Normal)
        self.passEntBox.bind("<KeyPress>", self.shortcut)

        self.loginButton = tk.Button(self.loginFrame, text="Login!")

        # widget placing
        self.titleLabel.pack(side="top")
        self.subTitleLabel.pack(side="top")
        self.titleFrame.pack(side="top")

        self.userLabel.grid(row=0, column=0, columnspan=2)
        self.userEntBox.grid(row=1, column=0, columnspan=2)
        self.passLabel.grid(row=0, column=3, columnspan=2)
        self.passEntBox.grid(row=1, column=3, columnspan=2)
        self.loginButton.grid(row=2, column=1, columnspan=3)
        self.loginFrame.pack(side="bottom", pady=10)

        if (not autoShow):
            self.root.withdraw()

    def setLoginButtonFunction(self, newFunc):
        self.loginFunc = newFunc
        self.loginButton.config(command=self.loginFunc)

    def startMainloop(self):
        self.root.mainloop()
    
    def shortcut(self, event):
        if (event.keysym == "Return"):
            self.loginFunc()
    
    def getUserStr(self):
        return self.userEntBox.get()
    
    def getPassStr(self):
        return self.passEntBox.get()
    
    def raiseWindow(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

    def quit(self):
        self.root.destroy()
    
class CustomerPage:
    def __init__(self, currentUserObj=None, autoShow=True):
        self.root = tk.Tk()
        self.root.geometry("600x380")

        if currentUserObj:
            self.currentUser = currentUserObj

        # tk vars
        self.optionSelect = tk.IntVar()
        self.opt3PplNum = tk.IntVar()

        # widgets making
        self.topNavPane = tk.Frame(self.root, height=25, width=600)
        self.choiceOrderButton = tk.Button(self.topNavPane, text="Order", font=config.Fonts.Small)
        self.choiceMySubsButton = tk.Button(self.topNavPane, text="My Subs", font=config.Fonts.Small)
        self.choiceAccountButton = tk.Button(self.topNavPane, text="Account", font=config.Fonts.Small)

        self.orderFrame = tk.Frame(self.root)
        self.orderOpt1Check = tk.Radiobutton(self.orderFrame, variable=self.optionSelect, value=1, command=self.orderUpdateWigdetsOnUserEvent)
        self.orderOpt1Text = tk.Label(self.orderFrame, text="What: Daily Crisp High Fives, every month\nCost: $49.99/mo")
        self.orderOpt1Text.bind('<Button-1>', lambda event: self.orderUpdateWigdetsOnUserEvent(setVarTo=1))

        self.orderOpt2Check = tk.Radiobutton(self.orderFrame, variable=self.optionSelect, value=2, command=self.orderUpdateWigdetsOnUserEvent)
        self.orderOpt2Text = tk.Label(self.orderFrame, text="What: Instant Crisp High Five\nCost: $5.99, plus $1.99 per mile of travel")
        self.orderOpt2Text.bind('<Button-1>', lambda event: self.orderUpdateWigdetsOnUserEvent(setVarTo=2))
        
        self.orderOpt3Check = tk.Radiobutton(self.orderFrame, variable=self.optionSelect, value=3, command=self.orderUpdateWigdetsOnUserEvent)
        self.orderOpt3Text = tk.Label(self.orderFrame, text="What: 10 Group High Fives plus extra\nCost: $49.99, plus $3.99 per extra high five")
        self.orderOpt3Text.bind('<Button-1>', lambda event: self.orderUpdateWigdetsOnUserEvent(setVarTo=3))
        self.orderOpt3PplText = tk.Label(self.orderFrame, text="# of people:")
        self.orderOpt3PplBox = tk.Spinbox(self.orderFrame, from_=10, to=690, command=self.orderUpdateWigdetsOnUserEvent)
        
        self.orderOpt4Check = tk.Radiobutton(self.orderFrame, variable=self.optionSelect, value=4, command=self.orderUpdateWigdetsOnUserEvent)
        self.orderOpt4Text = tk.Label(self.orderFrame, text="What: Custom High Five!\nCost: $22.99, plus $1.99 per mile of travel")
        self.orderOpt4Text.bind('<Button-1>', lambda event: self.orderUpdateWigdetsOnUserEvent(setVarTo=4))
        self.orderOpt4CustomText = tk.Label(self.orderFrame, text="Custom Interaction:")
        self.orderOpt4CustomBox = tk.Entry(self.orderFrame)

        self.orderNextButton = tk.Button(self.orderFrame, text="Next")

        # placing widgets
        self.root.columnconfigure(0, weight=1)

        self.choiceOrderButton.pack(side="left", fill="x")
        self.choiceMySubsButton.pack(side="left", fill="x")
        self.choiceAccountButton.pack(side="left", fill="x")
        self.topNavPane.grid(row=0)

        self.orderOpt1Check.grid(column=0, row=0)
        self.orderOpt1Text.grid(column=1, row=0, columnspan=2)
        self.orderOpt2Check.grid(column=0, row=1)
        self.orderOpt2Text.grid(column=1, row=1, columnspan=2)
        self.orderOpt3Check.grid(column=0, row=2)
        self.orderOpt3Text.grid(column=1, row=2, columnspan=2)
        self.orderOpt3PplText.grid(column=1, row=3)
        self.orderOpt3PplBox.grid(column=2, row=3)
        self.orderOpt4Check.grid(column=0, row=4)
        self.orderOpt4Text.grid(column=1, row=4, columnspan=2)
        self.orderOpt4CustomText.grid(column=1, row=5)
        self.orderOpt4CustomBox.grid(column=2, row=5)
        self.orderNextButton.grid(row=6, columnspan=3)
        self.orderFrame.grid(row=1, pady=10)

        if (not autoShow):
            self.root.withdraw()

        self.orderUpdateWigdetsOnUserEvent()
    
    def startMainloop(self):
        self.root.mainloop()

    def raiseWindow(self):
        self.root.deiconify()

    def orderUpdateWigdetsOnUserEvent(self, event=None, setVarTo=None):
        if setVarTo:
            self.optionSelect.set(setVarTo)
        
        if (self.optionSelect.get() != 3):
            self.orderOpt3PplBox.config(state=tk.DISABLED)
        else:
            self.orderOpt3PplBox.config(state=tk.NORMAL)

        if (self.optionSelect.get() != 4):
            self.orderOpt4CustomBox.config(state=tk.DISABLED)
        else:
            self.orderOpt4CustomBox.config(state=tk.NORMAL)
        
        if (event):
            if (event.keysym == "Return"):
                self.orderNextButton.focus_set()

    def quit(self):
        self.root.destroy()

class EmployeePage:
    def __init__(self, autoShow=True):
        self.root = tk.Tk()
        
        if (not autoShow):
            self.root.withdraw()
    
    def startMainloop(self):
        self.root.mainloop()

    def raiseWindow(self):
        self.root.deiconify()

    def quit(self):
        self.root.destroy()

class SignUpPage:
    def __init__(self, user=None, pswd=None, autoShow=True):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("High Five Club - Sign Up")

        self.mainLabel = tk.Label(self.root, text="Please sign up", font=config.Fonts.Title)
        self.secLabel = tk.Label(self.root, text="Enter info below:", font=config.Fonts.SubTitle)

        self.infoFrame = tk.Frame(self.root)
        self.usernameLabel = tk.Label(self.infoFrame, text="Username:")
        self.usernameBox = tk.Entry(self.infoFrame)
        self.usernameBox.insert(0, str(user))
        self.emailLabel = tk.Label(self.infoFrame, text="Email:")
        self.emailBox = tk.Entry(self.infoFrame)
        self.passLabel = tk.Label(self.infoFrame, text="Password:")
        self.passBox = tk.Entry(self.infoFrame)
        self.passBox.insert(0, str(pswd))

        self.signupButton = tk.Button(self.root, text="Sign Up", command=self.attemptSignup)

        self.mainLabel.pack()
        self.secLabel.pack()

        self.usernameLabel.grid(row=0, column=0)
        self.usernameBox.grid(row=0, column=1)
        self.emailLabel.grid(row=1, column=0)
        self.emailBox.grid(row=1, column=1)
        self.passLabel.grid(row=2, column=0)
        self.passBox.grid(row=2, column=1)
        self.infoFrame.pack()
        self.signupButton.pack()

        if (autoShow):
            self.root.mainloop()
    
    def attemptSignup(self):
        print(self.usernameBox.get(), self.emailBox.get(), self.passBox.get())
        attempt = auther.attemptAddAccount(self.usernameBox.get(), self.emailBox.get(), self.passBox.get(), False)
        if (attempt == -1):
            mbx.showerror(title="Sign Up Error!", message="Sorry, that username is taken. Please try a different one.")
        elif (attempt == 0):
            mbx.showinfo(title="Sign Up Success!", message="Sign Up successful! You will now be redirected to the customer page :)")
            self.hide()
            self.root.quit()
    
    def setUsername(self, newUsername):
        self.usernameBox.delete(0, tk.END)
        self.usernameBox.insert(0, newUsername)
    
    def setPswd(self, newPswd):
        self.passBox.delete(0, tk.END)
        self.passBox.insert(0, newPswd)

    def getUsername(self):
        return self.usernameBox.get()
    
    def getEmail(self):
        return self.emailBox.get()
    
    def getPassword(self):
        return self.passBox.get()
    
    def hide(self):
        self.root.withdraw()

    def startMainloop(self):
        self.root.mainloop()

class CurrentUser:
    def __init__(self):
        self.username = ""
        self.pswd = ""
    
    def setNewUser(self, username, pswd):
        self.username = username
        self.pswd = pswd
        
    def getUserInfo(self):
        return (self.username, self.pswd)