import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']





    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]



    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    pas = password_entry.get()
    mail = email_entry.get()

    new_data = {
        web: {
            "Email": mail,
            "Password": pas,
    }}

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="Dont leave any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")

    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"email : {email} \npassword : {password} ")
        else:
            messagebox.showinfo(title="Error", message=f"There are no such details saved for the {website}.")

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)



canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website = Label(text="Website:")
website.grid(column=0, row=1)

password = Label(text="Password:")
password.grid(column=0, row=3)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

generate_pass = Button(text="Generate password", command=generate_password)
generate_pass.grid(column=2, row=3)


website_entry = Entry(width=28)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=47)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mjbhavit1234@gmail.com")
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)

add = Button(text="Add", width=36, command=save, highlightthickness=0)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=13, highlightthickness=0, command=find_password)
search.grid(column=2, row=1, columnspan=2)






window.mainloop()