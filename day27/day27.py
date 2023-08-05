# def add(*args):
#   sum = 0
#   for number in args:
#     sum += number
#   print(sum)
# add(3, 5, 2, 1, 5, 2, 9, 10, 13)

# import tkinter

# def onClickButton():
#   title["text"] = user_input.get()

# window = tkinter.Tk()
# window.geometry("500x500")

# title = tkinter.Label(text = "This is my title.")
# title.grid(row = 0, column = 0)

# button = tkinter.Button(text = "Click Me!", command = onClickButton)
# button.grid(row = 1, column = 1)

# new_btn = tkinter.Button(text = "no, Click me!")
# new_btn.grid(row=0, column = 3)


# user_input = tkinter.Entry(width=10)
# user_input.grid(row=2, column=4)




# window.mainloop()

import tkinter as tk

window = tk.Tk()
window.geometry("400x200")
window.configure(padx=30, pady=30)

user_input = tk.Entry(width=10)
user_input.grid(row=0, column=1)

miles = tk.Label(text="Miles")
miles.grid(row = 0, column=2)

is_equal_to = tk.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

output = tk.Label(text="0")
output.grid(row=1, column = 1)

kilometers = tk.Label(text='km')
kilometers.grid(row=1, column =2 )

def calculate_to_km():
  miles = int(user_input.get()) * 1.609
  output['text'] = miles

calculate = tk.Button(text="Calculate", command= calculate_to_km)
calculate.grid(row=2, column=1)


window.mainloop()
