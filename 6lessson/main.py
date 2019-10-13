import tkinter
import random

window = tkinter.Tk()
window.title("My window")
window.geometry("600x500")

label = tkinter.Label(text="0", fg="black", bg="red", font="Arial 22")
label.place(x=25, y=25)

def random_colors():
    colors = ["red", "green", "blue", "gray"]
    label["bg"] = random.choice(colors)

def count():
    random_colors()
    num = int(label["text"])
    num = num + 1
    label["text"] = str(num)

    
button = tkinter.Button(text="кнопка", command=count)
button.place(x=25, y=100)



window.mainloop()