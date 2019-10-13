from course import get_course
import tkinter

window = tkinter.Tk()
window.geometry("400x350")
window.title("Курс вылют")


img_logo = tkinter.PhotoImage(file="C:/Users/Илья/Desktop/my projects/pythonlessons/6lessson/logo.png")
logo = tkinter.Label(image=img_logo)
logo.place(x=0, y=0)

lab = tkinter.Label(text="Курс вaлют \n MAXIMUM банк", fg="black", font="Arial 22")
lab.place(x=150, y=25)

usd_course = tkinter.Label(text=f"$ {get_course('R01235')}", font="Arial 16")
usd_course.place(x=90, y=150)

eur_course = tkinter.Label(text=f"€ {get_course('R01239')}", font="Arial 16")
eur_course.place(x=90, y=190)


window.mainloop()
