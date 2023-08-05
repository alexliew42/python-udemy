# def add(*args):
#   sum = 0
#   for number in args:
#     sum += number
#   print(sum)
# add(3, 5, 2, 1, 5, 2, 9, 10, 13)

import tkinter

def onClickButton():
  title["text"] = "button got clicked"

window = tkinter.Tk()
window.geometry("500x500")

title = tkinter.Label(text = "This is my title.")
title.pack()

button = tkinter.Button(text = "Click Me!", command = onClickButton)
button.pack()



window.mainloop()

