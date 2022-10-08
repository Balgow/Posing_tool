from tkinter import * 
import tkinter as tk
import os


def takephoto():
    os.system('python takephoto.py')

def pose():
    os.system('python showlandmarks.py')

root  = tk.Tk()

root.title('Posing Tool')

root.geometry('500x500')

root.resizable(width=True, height=True)


canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg = 'red')
frame.place(relx = 0.15, rely = 0.15, relwidth=0.7, relheight=0.7)

title  = Label(frame, text='Posing Tool', bg='gray', font = 40)
title.pack()

btn_take_photo = Button(frame, text= 'Take photo', bg = 'yellow', command=takephoto)
btn_take_photo.pack()

btn_pose = Button(frame, text= 'Pose', bg = 'yellow', command=pose)
btn_pose.pack()

root.mainloop()