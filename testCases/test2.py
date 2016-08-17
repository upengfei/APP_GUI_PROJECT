from Tkinter import *

master = Tk()

def callback(event):
    print 'click at:'

frame = Frame(master,width=400,height=100)

frame.bind('<Return>',lambda e:'dagfa')
frame.pack()
master.mainloop()