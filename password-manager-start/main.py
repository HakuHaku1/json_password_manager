from tkinter import *
import string
import random
import json
from tkinter import messagebox

def gen_command():
    letters = string.ascii_letters     
    digits = string.digits              
    symbols = string.punctuation 

    Password_format = letters + digits + symbols

    password_gen = ''.join([random.choice(Password_format) for i in range(0,12)])
    password.delete(0, END)
    password.insert(0, f"{password_gen}")

def save():
    website_get = website.get()
    user_get = email_username.get()
    password_get = password.get()
    confirm = messagebox.askokcancel(title= "MyPass app", message= f"These are the details entered: \n{user_get}\nPassword: {password_get}")
    if not confirm:
        password.delete(0, END)
        website.delete(0,END)
        email_username.delete(0,END) 
    else:
        if not website_get or not password_get or not user_get:
            messagebox.showerror(title= "MyPass app",message="the input you entered has some missing entry")
        else: 
            update_data = {
                website_get: {
                "email" : user_get, 
                "password": password_get,
                }
            }
            try:
                with open(file= "data.json", mode= "r") as file:
                    data = json.load(file)
                    data.update(update_data)
                with open(file = "data.json", mode = "w") as file:

                    json.dump(data, file, indent= 4)
            except FileNotFoundError:
                messagebox.showerror(title= "MyPass app",message="file not found")
            finally:
                password.delete(0, END)
                website.delete(0,END)
                email_username.delete(0,END)  

def searching():
    website_get = website.get()
    user_get = email_username.get()
    with open(file= "data.json", mode= "r") as file:
        data = json.load(file)

    if website_get in data and user_get in data[website_get]["email"] == user_get:
        messagebox.showinfo(title= "MyPass app",message= f"MATCH FOUND\n{user_get} \nPassword {data[website_get]["password"]}")
    elif not website_get in data:
        messagebox.showerror(title= "MyPass app",message=f"invalid website: {website_get}")
    elif not user_get in data[website_get]["email"] == user_get:
        messagebox.showerror(title= "MyPass app",message= f"invalid email: {user_get}")


window = Tk()
window.config(padx= 20, pady= 20, bg= "black")
window.title("password manager")

canva = Canvas(window, width=200, height=200, highlightthickness=0, bg= "black")
canva.grid(row=0, column=3, columnspan=6)

image = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=image)

website = Entry(window, width= 40)
website.grid(row=1, column=3, columnspan= 3)

label_website = Label(text= "website: ", font= ("courier", 9), fg= "white", bg= "black")
label_website.grid(row= 1, column=0)

email_username = Entry(width= 70)
email_username.grid(row=3, column=3, columnspan= 5, pady= 20 )
label_email= Label(text= "email: ", font= ("courier", 9),fg= "white", bg= "black")
label_email.grid(row= 3, column=0)

password = Entry(window, width= 40)
password.grid(row=4, column=3, columnspan= 3  )
label_password = Label(text= "Password: ", font= ("courier", 9),fg= "white", bg= "black")
label_password.grid(row= 4, column= 0)

password_generator = Button(text= "Password generator",width= 22, height= 1, fg= "white", bg= "red",  command= gen_command)
password_generator.grid(row= 4, column= 7, columnspan= 8)

search = Button(text= "search",width= 22, height= 1,  fg= "white", bg= "red", command= searching)
search.grid(row= 1, column= 7, columnspan= 8)
add = Button(text= "add",width= 70, height= 1,  fg= "white", bg= "red", command= save)
add.grid(row= 5, column= 0, columnspan= 8, pady= 10)

window.mainloop()