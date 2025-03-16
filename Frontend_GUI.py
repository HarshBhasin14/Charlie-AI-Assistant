from tkinter import *
import tkinter as tk
from PIL import Image
from playsound import playsound
from threading import Thread

root = tk.Tk()

#anim2

file1 = r"C:\Users\Computer Clinic\Downloads\final_5ffa7f71eeb46f00a88f8902_656357.gif"
 
info1 = Image.open(file1)

frames = info1.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file1,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation_1(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

#anim2

root.title("Charlie v.1.0")
file='D:\Wallpapers\Jarvis.gif'              

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))
    
def stop_animation():
    root.after_cancel(anim)

gif_label = tk.Label(root,image="", width=350,height=400,bg='black')
gif_label.pack()

animation_1(count)

def sound():
    playsound(r'C:\Users\Computer Clinic\Downloads\Need For Speed Shift - Intro-[AudioTrimmer.com].wav')
Thread(target = animation).start()
Thread(target = sound).start()
    

root.mainloop()