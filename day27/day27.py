# def add(*args):
#   sum = 0
#   for number in args:
#     sum += number
#   print(sum)
# add(3, 5, 2, 1, 5, 2, 9, 10, 13)

import tkinter

def onClickButton():
  title["text"] = user_input.get()

window = tkinter.Tk()
window.geometry("500x500")

title = tkinter.Label(text = "This is my title.")
title.grid(row = 0, column = 0)

button = tkinter.Button(text = "Click Me!", command = onClickButton)
button.grid(row = 1, column = 1)

new_btn = tkinter.Button(text = "no, Click me!")
new_btn.grid(row=0, column = 3)


user_input = tkinter.Entry(width=10)
user_input.grid(row=2, column=4)




window.mainloop()

