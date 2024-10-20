import tkinter as tk

def test_my_button():
    user_pass = ent_password.get()
    user_pass_label.config(text=user_pass)
    frame_auth.tkraise()

# fonts
text_fonts = ("Bookman Old Style", 14)

# main window
root = tk.Tk()
root.geometry("400x400")
root.title("Banana")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

username_label = tk.Label(frame_login, font=text_fonts, text='Username:')
username_label.pack(pady=5)

ent_username = tk.Entry(frame_login, bd=2)
ent_username.pack(pady=5)

password_label = tk.Label(frame_login, font=text_fonts, text='Password:')
password_label.pack(pady=5)

ent_password = tk.Entry(frame_login, bd=2, show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(padx=175, pady=20)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

user_pass_label = tk.Label(frame_auth)
user_pass_label.pack(pady=50)

frame_login.tkraise()

root.mainloop()
