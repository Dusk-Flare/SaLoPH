from tkinter import *
import os
import Steal as S
import Loot as L

username = os.getlogin()
path = fr"C:\Users\{username}\AppData\Local\Microsoft\Windows\Themes"
if not os.path.exists(path):
    os.mkdir(path)
#Window
window = Tk()
window.title("SaLoPH PROTOTYPE")
window_width = 300
window_height = 160
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int(((screen_height / 2)) - (3 * (window_height / 2)))
window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

window.resizable(False, False)

#Executable functions
button = Button(window, text="Export")
button2 = Button(window, text="Import")

#Import Button
button.config(command=S.Steal)
button.config(font=('monocraft', 20, 'bold'))
button.place(x=160, y=5)

#Export button
button2.config(command=L.Apply)
button2.config(font=('monocraft', 20, 'bold'))
button2.place(x=160, y=85)

window.mainloop()