from tkinter import *
from tkinter import messagebox
import sys
from PIL import ImageGrab
from tensorflow_chessbot import main

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

window = Tk()
window.title("Chess board parser")

Grid.rowconfigure(window, 0, weight=0)
Grid.rowconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 0, weight=1)

TMP_FILENAME = 'tmp.png'

def imgps():
    try:
        im = ImageGrab.grabclipboard()
        im.save(TMP_FILENAME)
    except BaseException as err:
        messagebox.showinfo(message="Clipboard is Empty.")
        return

    try:
        main(dotdict({
            'filepath': TMP_FILENAME
        }))
    except BaseException as err:
        redirector(str(err))

pbtn11 = Button(window, text="Parse from clipboard", command=imgps)
pbtn11.grid(row=0, sticky='nsew')

textbox=Text(window, font="TkFixedFont")
textbox.grid(row=1, sticky='nsew')

def redirector(inputStr):
    textbox.insert(INSERT, inputStr + '\n')

sys.stdout.write = redirector
print('OUTPUT')

window.mainloop()