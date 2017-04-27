#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script centers a small
window on the screen.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Frame, BOTH


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.initUI()


    def initUI(self):

        self.parent.title("Quit button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=50, y=50)


    def centerWindow(self):

        w = 100
        h = 450

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        w = sw/1.75
        h = sh/1.75
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
