from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  website_input = website_entry.get()
  email_input = email_entry.get()
  password_input = password_entry.get()
  f = open('data.txt', 'a')
  f.write(f'{website_input} | {email_input} | {password_input}\n')
  website_entry.delete(0, "end")
  password_entry.delete(0, "end")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)


lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#LABELS
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

#ENTRIES
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "liewtwoo42@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#BUTTONS
generate_button = Button(text="Generate Button")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()