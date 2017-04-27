from Tkinter import *

def func1():
    print("in func1")

def func2():
    print("in func2")

def selection():
    try:
        dictionary[listbox.selection_get()]()
    except:
        pass

root = Tk()

frame = Frame(root)
frame.pack()

dictionary = {"1":func1, "2":func2}

items = StringVar(value=tuple(sorted(dictionary.keys())))

listbox = Listbox(frame, listvariable=items, width=15, height=5)
listbox.grid(column=0, row=2, rowspan=6, sticky=("n", "w", "e", "s"))
listbox.focus()

selectButton = Button(frame, text='Select', underline = 0, command=selection)
selectButton.grid(column=2, row=4, sticky="e", padx=50, pady=50)

root.bind('<Double-1>', lambda x: selectButton.invoke())

root.mainloop()


# from Tkinter import *
# import tkMessageBox
# import Tkinter
#
# top = Tk()
#
#
#
# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
#
# Lb1.pack()
# top.mainloop()

## TODO Click event
## TODO Double Click event
## TODO back event
## TODO show folders, pdf files
##

# from Tkinter import *
# import tkFont
# # using grid
# # +------+-------------+
# # | btn1 |    btn2     |
# # +------+------+------+
# # | btn3 | btn3 | btn4 |
# # +-------------+------+
# root = Tk()
# # tkFont.BOLD == 'bold'
# helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
# btn1 = Button(text='btn1', font=helv36)
# btn2 = Button(text='btn2', font=helv36)
# btn3 = Button(text='btn3', font=helv36)
# btn4 = Button(text='btn4', font=helv36)
# btn5 = Button(text='btn5', font=helv36)
# root.rowconfigure((0,1), weight=1)  # make buttons stretch when
# root.columnconfigure((0,2), weight=1)  # when window is resized
# btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS')
# btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
# btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS')
# btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS')
# btn5.grid(row=1, column=2, columnspan=1, sticky='EWNS')
#
# root.mainloop()
#
# # #!/usr/bin/python
# # # -*- coding: utf-8 -*-
# #
# # """
# # ZetCode Tkinter tutorial
# #
# # This script centers a small
# # window on the screen.
# #
# # Author: Jan Bodnar
# # Last modified: November 2015
# # Website: www.zetcode.com
# # """
# #
# # from Tkinter import Tk, Frame, BOTH
# # from ttk import Button, Style
# # class Example(Frame):
# #
# #     def __init__(self, parent):
# #         Frame.__init__(self, parent, background="white")
# #
# #         self.parent = parent
# #         self.parent.title("Centered window")
# #         self.pack(fill=BOTH, expand=1)
# #         self.centerWindow()
# #
# #         self.initUI()
# #
# #
# #     def initUI(self):
# #
# #         self.parent.title("Quit button")
# #         self.style = Style()
# #         self.style.theme_use("default")
# #
# #         self.pack(fill=BOTH, expand=1)
# #
# #         quitButton = Button(self, text="Quit",
# #             command=self.quit)
# #         quitButton.place(x=450, y=450, height=70, width=200)
# #
# #
# #     def centerWindow(self):
# #
# #         w = 100
# #         h = 450
# #
# #         sw = self.parent.winfo_screenwidth()
# #         sh = self.parent.winfo_screenheight()
# #         w = sw/1.75
# #         h = sh/1.75
# #         x = (sw - w)/2
# #         y = (sh - h)/2
# #         self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
# #
# #
# # def main():
# #
# #     root = Tk()
# #     ex = Example(root)
# #     root.mainloop()
# #
# #
# # if __name__ == '__main__':
# #     main()
