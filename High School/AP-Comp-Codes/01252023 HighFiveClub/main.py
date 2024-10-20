import tkinter as tk
from tkinter import messagebox as mbx
import classes as cls
import authenticator as auther


loginPage = cls.LoginPage(autoShow=False)
signupPage = None
customerPage = cls.CustomerPage(autoShow=False)
employeePage = cls.EmployeePage(autoShow=False)
currentUser = cls.CurrentUser()

def auth(user, pswd):
    return auther.attemptLogin(user, pswd)

def getPageObject(type):
    if (type == "customer"):
        return cls.CustomerPage()
    elif (type == "employee"):
        return cls.EmployeePage()
    return cls.LoginPage()  # only here for fixing an "error"

def loginFunc(username=None, password=None):  # parameters used for feeding in from sign up
    if not username or not password:
        user = loginPage.getUserStr()
        pswd = loginPage.getPassStr()
    else:
        user = username
        pswd = password
    print(user, pswd)
    tryAuth = auth(user, pswd)
    if (tryAuth == 0):
        # open customer page
        if not username or not password:
            mbx.showinfo(title="Success!", message="Successfully logged in as customer!")
        loginPage.hide()
        customerPage = cls.CustomerPage(currentUser)
    elif (tryAuth == 1):
        # open employee page
        mbx.showinfo(title="Success!", message="Successfully logged in as employee!")
        loginPage.hide()
        employeePage.startMainloop()
        employeePage.raiseWindow()
    elif (tryAuth == -2):
        mbx.showinfo(title="Failure.", message=f"Error! Incorrect password for the account with username/email: {user}")
    elif (tryAuth == -1):
        createNew = mbx.askokcancel(title="Create Account?", message="There is no account created with this Username or Email. Would you like to create a new one?")
        if createNew:
            signupPage = cls.SignUpPage(user, pswd, autoShow=False)
            signupPage.setUsername(user)
            signupPage.setPswd(pswd)
            signupPage.startMainloop()
            user = signupPage.getUsername()
            pswd = signupPage.getPassword()

    print("attempt: " + str(tryAuth))

loginPage = cls.LoginPage()
loginPage.setLoginButtonFunction(loginFunc)
loginPage.startMainloop()

# customerPage = getPageObject("customer")
# customerPage.startMainloop()
