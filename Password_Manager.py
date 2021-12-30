from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BACKGROUND = "#427996"
LABEL_FG = "white"
INPUT_BG = '#F2FFE9'
BUTTON_COLOR = "#4C5F7A"
BUTTON_FG = "white"
ACTIVE_BUTTON_FG = "#557C55"
ACTIVE_BUTTON_BG =  "#555555"
# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    global content
    word = website_input.get()
    key = word.lower()
    try:
        with open("data.json","r") as data_file:
            content=json.load(data_file)
    except FileNotFoundError:
            content = {}
    finally:
        value = content.get(key)
        if value is None:
            messagebox.showerror(title=word,message="Info for website: " + str(word) + " not found!")
        else:
            username = value.get("username")
            password = value.get("password")
            messagebox.showinfo(title=word,message="Email:" + str(username) + " \nPassword: " + str(password))




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
        
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save():
    global data
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {website:{"username":username,"password": password}}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Eroare", message="Va rog sa completati toate casutele!")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
                data = new_data
        finally:
            with open("data.json","w") as data_file:
                json.dump(data,data_file, indent=4)
            website_input.delete(0,END)
            password_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.iconphoto(False,PhotoImage(file='icon.png'))
#window.geometry("500x500")
window.config(padx=20, pady=20, bg=BACKGROUND)

canvas = Canvas(width=220, height=220, highlightthickness=0, bg=BACKGROUND)
canvas.grid(row=0, column=1, sticky="NW")
image = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image= image)


#Website

website_label = Label(text="Website:", fg=LABEL_FG, bg=BACKGROUND)
website_label.grid(row=2, column=0, sticky="S")

website_input = Entry(width = 35, relief="flat", bg=INPUT_BG)
website_input.grid(row=2,column = 1, columnspan=2, sticky="W")
website_input.focus()
#Email/Username

username_label = Label(text="Email/Username:", fg=LABEL_FG, bg=BACKGROUND)
username_label.grid(row=3, column=0)

username_input = Entry(width = 58, relief="flat", bg=INPUT_BG)
username_input.grid(row=3,column = 1, columnspan=2, sticky="W")
username_input.insert(0,"veronica.moldovan94@outlook.com")
#Password

password_label = Label(text="Password:", fg=LABEL_FG, bg=BACKGROUND)
password_label.grid(row=4, column=0)

password_input = Entry(width=35, exportselection=1, relief="flat", bg=INPUT_BG)
password_input.grid(row=4,column = 1, sticky="W")

generator = Button(
    text="Generate Password",
    width=17,
    fg=BUTTON_FG,
    activebackground=ACTIVE_BUTTON_FG,
    activeforeground=ACTIVE_BUTTON_BG,
    bg=BUTTON_COLOR,
    relief="groove",
    command=pass_generator)
generator.grid(row=4, rowspan= 1, column=2,sticky="SE")

#Add Button

add_button = Button(
    text="Add",
    width=49,
    fg=BUTTON_FG,
    activebackground=ACTIVE_BUTTON_FG,
    activeforeground=ACTIVE_BUTTON_BG,
    bg=BUTTON_COLOR,
    relief="groove",
    command=pass_save)
add_button.grid(row=5,column=1,columnspan=2, sticky = "E")

search_button = Button(
    text="Search",
    width=17,
    fg=BUTTON_FG,
    activebackground=ACTIVE_BUTTON_FG,
    activeforeground=ACTIVE_BUTTON_BG,
    bg=BUTTON_COLOR,
    relief="groove",
    command=search)
search_button.grid(row=2,column=1,columnspan=2, sticky = "E")














window.mainloop()