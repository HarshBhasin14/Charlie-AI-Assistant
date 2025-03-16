from tkinter import *
import tkinter as tk
from PIL import Image
from playsound import playsound
from threading import Thread

root = tk.Tk()
root.title("Charlie v.1.0")
file= r'E:\Charlie\Media\Jarvis.gif'

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

animation(count)
a=0
def sound():
    playsound(r'E:\Charlie\Media\Need For Speed Shift - Intro-[AudioTrimmer.com].wav')
Thread(target = animation).start()
Thread(target = sound).start()
    
root.after(10000, lambda: root.destroy())
root.mainloop()