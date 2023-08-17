from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project 
import random
import json

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  password_list = [random.choice(letters) for char in range(nr_letters)]
  password_list += [random.choice(symbols) for char in range(nr_symbols)]
  password_list += [random.choice(numbers) for char in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)

  password_entry.delete(0, "end")
  password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  website_input = website_entry.get()
  email_input = email_entry.get()
  password_input = password_entry.get()

  new_data = {
    website_input: {
      "email": email_input,
      "password": password_input
  }
}

  if len(website_input) == 0 or len(password_input) == 0 or len(email_input) == 0:
    messagebox.showinfo(title="woops",message="You can't leave any field empty!")
  else:
    is_ok = messagebox.askokcancel(title=website_input, message=f'These are the details entered: \nEmail: {email_input}\nPassword: {password_input}.\nIs it ok to save?')
    
    if is_ok:
        f = open('data.json', 'r')
        # json.dump(new_data, f, indent=4)
        data = json.load(f)
        data.update(new_data)

        with open("data.json", 'w') as f:
          json.dump(data, f, indent=4)
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
generate_button = Button(text="Generate Button", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

# fruits = ["Apple", "Pear", "Orange"]

# #todo: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#       fruit = fruits[index]
#     except IndexError: 
#       print('Fruit pie')
#     else: 
#       print(fruit + " pie")



# make_pie(2)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#       total_likes = total_likes + post['Likes']
#     except KeyError:
#       total_likes += 0



# print(total_likes)